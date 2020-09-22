#For each SARS-CoV-2 global lineage, produces:
#A) A global map with sequence distribution labelled as points
#B) A bar chart showing the number of sequences from each country
#C) A histogram of sample collection dates
#Takes a sample metadata csv file and a file containing country latitude and longitude coordinates as input.
#The sample metadata file needs to contain the following columns:
#lineage - used to define the global lineage the sequence belongs to
#sample_date - the date the sample was collected in format day/month/year, e.g. 20/01/2020
#country - the country the sample was collected in
#To run: RScript lineage_distributions.R sample_metadata.csv country_coordinates.csv

args <- commandArgs(TRUE)

library(stringr)
library(ggplot2)
library(grid)
library(cowplot)

# Select all sequence labels matching a cluster name using cluster lookup table
getClusterIds <- function(clusterNames, clusters) as.character(clusters$sequence_label[clusters$lineage %in% clusterNames])

#Extracts the descendent lineages of a given lineage
getDescendents <- function(lineage, uniqueLineages) { #Extracts the descendent lineages of a given lineage
  downstreamLineages <- (c(as.matrix(uniqueLineages[grep(lineage, uniqueLineages)])))
  
  classificationLevel <- str_count(lineage, "\\.") #The classication level of the lineage, descendent lineages will have a higher classification level
  descendents <- c(lineage)
  
  for (eachLineage in downstreamLineages) {
    if (eachLineage != lineage & (str_count(eachLineage, "\\.") > classificationLevel)) {
      descendents <- c(descendents, eachLineage)}}
  
  return(descendents)}

countryConversion <- function(locations, conversion) { #Takes a set of locations and converts them if they are in a list
  for (location in 1:length(locations)) { #Iterate through the locations and check if they need to be converted
    if (locations[location] %in% conversion[,1]) {
      locations[location] <- toString(conversion[which(conversion[,1] == toString(locations[location])),2])}}
  
  return(locations)}

#Import the cluster metadata
clusters <- read.csv(args[1])

#Import the country latitude longitudes and continents
countryLatitudeLongitude <- read.csv(args[2])

#Replace country names in metadata that do not match those in the latitude longitude table
clusters$country[which(clusters$country == "United_States")] <- "USA"
clusters$country[which(clusters$country == "ISRAEL")] <- "Israel"
clusters$country[grep("Romania", clusters$country)] <- "Romania"

#Extract the unique lineages
uniqueLineages <- unique(clusters$lineage)

#Convert the collection dates to dates
clusters$Date <- as.Date(clusters$sample_date)

#Plot the world map onto which lineage locations will be plotted
worldMap <- map_data('world')

#Set the colours for the continents in each plot
continentColours <- c("red", "yellow4", "dodgerblue", "darkorange", "purple", "magenta")
names(continentColours) <- c("Africa", "Asia", "Europe", "NorthAmerica", "Oceania", "SouthAmerica")

#Add the continents to clusters
clusters$Continent <- ""
for (eachCountry in 1:length(clusters[,1])) {
  clusters$Continent[eachCountry] <- toString(countryLatitudeLongitude[which(countryLatitudeLongitude[,1] == toString(clusters$country[eachCountry])),4])}

#Iterate through the lineages and plot their distribution
for (lineage in uniqueLineages) {
  svglite::svglite(paste(lineage, ".svg", sep = ""))
  
  #Identify the descendent lineages and extract the sequences within the lineage
  descendentLineages <- getDescendents(lineage, uniqueLineages)
  lineageSamples <- clusters[which(clusters$lineage %in% descendentLineages),]
  
  #Extract the countries the lineage is located in
  uniqueCountries <- unique(lineageSamples$country)

  #Will be filled with the number of sequences in each country within the lineage
  countrySamples <- data.frame(matrix(0, ncol = 5, nrow = length(uniqueCountries)))
  names(countrySamples) <- c("Country", "Latitude", "Longitude", "Continent", "NumberOfSamples")
  
  #Iterate through the countries and add their locations and number of sequences to countrySamples
  for (country in 1:length(uniqueCountries)) {
    countrySamples[country,1] <- toString(uniqueCountries[country])
    countrySamples[country,2] <- countryLatitudeLongitude[which(countryLatitudeLongitude[,1] == toString(uniqueCountries[country])),2]
    countrySamples[country,3] <- countryLatitudeLongitude[which(countryLatitudeLongitude[,1] == toString(uniqueCountries[country])),3]
    countrySamples[country,4] <- toString(countryLatitudeLongitude[which(countryLatitudeLongitude[,1] == toString(uniqueCountries[country])),4])
    countrySamples[country,5] <- length(which(lineageSamples$country == uniqueCountries[country]))}
  
  baseWorld <- ggplot() + coord_fixed() + xlab('') + ylab('') + geom_polygon(data=worldMap,aes(x=long,y=lat,group=group),colour='grey',fill='grey') + theme_void()
  mapData <- baseWorld + geom_point(data = countrySamples, aes(x = Longitude, y = Latitude, size = NumberOfSamples, colour = Continent), alpha = 0.5) + scale_colour_manual(name = "Continent", values = continentColours) + guides(size = FALSE, color = FALSE)
  
  #Sort by the number of samples from the country for plotting
  sortedCountrySamples <- countrySamples[order(-countrySamples$NumberOfSamples),]
  sortedCountrySamples$CountryFactor <- factor(sortedCountrySamples$Country, levels = sortedCountrySamples$Country)
  
  countryPlot <- ggplot(sortedCountrySamples, aes(x = CountryFactor, y = NumberOfSamples, fill = Continent)) + theme_bw() + geom_bar(stat = "identity") + scale_fill_manual(name = "Continent", values = continentColours) + theme(axis.text.x = element_text(angle = 270, size = 5), legend.title = element_text(size = 8), legend.text = element_text(size = 8)) + xlab("Country") + ylab("Number of\nsequences")
  datePlot <- ggplot(lineageSamples, aes(x = Date, fill = Continent)) + theme_bw() +  geom_histogram(binwidth = 1) + scale_fill_manual(name = "Continent", values = continentColours) + ylab("Number of sequences") + guides(fill = FALSE)
  
  minimumDateDay <- strsplit(toString(min(lineageSamples$Date)), "-")[[1]][3]
  minimumDateMonth <- strsplit(toString(min(lineageSamples$Date)), "-")[[1]][2]
  minimumDateYear <- strsplit(toString(min(lineageSamples$Date)), "-")[[1]][1]
  maximumDateDay <- strsplit(toString(max(lineageSamples$Date)), "-")[[1]][3]
  maximumDateMonth <- strsplit(toString(max(lineageSamples$Date)), "-")[[1]][2]
  maximumDateYear <- strsplit(toString(max(lineageSamples$Date)), "-")[[1]][1]
  
  lineageLabel <- textGrob(paste("Lineage ", lineage, ": ", length(lineageSamples[,1]), " sequences sampled ", minimumDateDay, "/", minimumDateMonth, "/", minimumDateYear, "-", maximumDateDay, "/", maximumDateMonth, "/", maximumDateYear, " from ", length(countrySamples[,1]), " countries on ", length(unique(countrySamples$Continent)), " continents", sep = ""), gp = gpar(fontsize = 12))
  figureLabel <- textGrob(paste("Lineage ", lineage, " sequence distributions. (A) Map of Lineage ", lineage, " global sampling locations. Point size is proportional to the number\nof sequences from the country. (B) Number of Lineage ", lineage, " sequences collected from each country. (C) Collection day of Lineage ", lineage, " sequences.", sep = ""), gp = gpar(fontsize = 10))
  
  combinedPlot <- plot_grid(lineageLabel, mapData, countryPlot, datePlot, figureLabel, labels = c(NA, "A", "B", "C"), ncol = 1, rel_heights = c(0.04, 0.3, 0.3, 0.3, 0.06))
  print(combinedPlot)
  dev.off()}