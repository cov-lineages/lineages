
from collections import defaultdict
from collections import Counter
import imp
import pandas as pd
from epiweeks import Week,Year

classes = imp.load_source("class_defs", 'utils/class_defs.py')
time = imp.load_source("time_functions", "utils/time_functions.py")


def parse_travel_history(lin_obj_dict, tax_dict, metadata):

    with open(metadata) as f:
        next(f)
        for l in f:
            toks = l.strip("\n").split(",")
            travel = toks[2]
            name = toks[0]
          
            if travel != "":

                if name in tax_dict.keys():
                    
                    from_country = travel.split("/")[0]
                    
                    tax_dict[name].travel_history = (from_country,tax_dict[name].country)


    for lin_name, lin_obj in lin_obj_dict.items():
        for_counting = []
        for tax in lin_obj.taxa:
            if tax.travel_history:
                
                from_c = tax.travel_history[0]
                to_c = tax.travel_history[1]

                for_counting.append(from_c)
                
                lin_obj.travel_history[from_c].add(to_c)

        lin_obj.travel_counts = Counter(for_counting)

    return lin_obj_dict

def sortkey2(taxon):
    return taxon.date_dt

def make_objects(metadata_file):

   
    #epiweeks = time.make_epiweeks()

    lineage_objects = []
    taxa = []
    tax_dict = {}
    tax_with_dates = []
    lineages_to_taxa = defaultdict(list)
    lin_obj_dict = {}

    with open(metadata_file) as f:
        next(f)
        for l in f:
           
            toks = l.strip("\n").split(",")
            
            tax_name = toks[0]
            country = toks[1]
            date = toks[3]
            epiweek = toks[4]
            lin_string = toks[5]

            metadata = [country, date, epiweek]
            
            new_taxon = classes.taxon(tax_name, lin_string, metadata)
            taxa.append(new_taxon)
            if new_taxon.date_dt != "NA":
                tax_with_dates.append(new_taxon)

            tax_dict[tax_name] = new_taxon
            
            lineages_to_taxa[lin_string].append(new_taxon)


    current_date = sorted(tax_with_dates, key=sortkey2, reverse = True)[0].date_dt
    current_week = Week.fromdate(current_date)
    
    for lin, lin_specific_taxa in lineages_to_taxa.items():
        l_o = classes.lineage(lin, lin_specific_taxa, current_date, current_week)

        lin_obj_dict[lin] = l_o


    lin_obj_dict = parse_travel_history(lin_obj_dict, tax_dict, metadata_file)

    return lin_obj_dict, taxa, current_date


def sort_key(lin):
    return len(lin.taxa)


def make_dataframe(lin_obj_dict):

    dataframe_dict = defaultdict(list)

    for i in lin_obj_dict.values():
        #print(i.id, i.mrd, i.oldest, i.main_locs)
        
        dataframe_dict["Lineage name"].append(i.id)
        dataframe_dict["Most common countries"].append(i.mains_plus_freqs)
        dataframe_dict["Date range"].append(i.pretty_oldest + " to " + i.pretty_mrd)
        dataframe_dict["Number of taxa"].append(len(i.taxa))
        dataframe_dict["Days since last sampling"].append(i.last_sampled)
        dataframe_dict["Known Travel"].append(i.travel_history)

    dataframe = pd.DataFrame(dataframe_dict)

   
    
    new_countries_list = []
    for i in dataframe["Most common countries"]:
        new_countries = str(i).strip("[").strip("]").replace("'","")
        new_countries_list.append(new_countries)
    dataframe["Most common countries"] = new_countries_list

    new_dates = []
    for i in dataframe["Date range"]:
        new_date = str(i).strip("(").strip(")").replace("'","")
        new_dates.append(new_date)
    dataframe["Date range"] = new_dates

    new_travels = [] 
    
    for index, row in dataframe.iterrows():
        subset = []
        mydict = row["Known Travel"]
        lin = lin_obj_dict[row["Lineage name"]]
        for key, st in mydict.items():
            counts = lin.travel_counts[key]
            subset.append(key + " to " + ", ".join(i for i in st) + ' (' + str(counts) + ")<br/>")
        
        subset = str(subset).strip("[").strip("]").replace("'", "").replace("<br/>,","<br/>")
    
        new_travels.append(subset)


    dataframe["Known Travel"] = new_travels

    dataframe.sort_values(by=["Number of taxa"], ascending=False, inplace=True)

    dataframe.set_index("Lineage name", inplace=True)


    return dataframe


def describe_lineages(lineage_objects):

    statuses = []
    reactivated_lineages = []
    continuing_lineages = []

    for lin in lineage_objects:
        statuses.append(lin.status)
        if lin.status == "Reactivated":
            reactivated_lineages.append(lin)
        elif lin.status == "Continuing":
            continuing_lineages.append(lin)
    
    status_counts = Counter(statuses)
    

    return status_counts, reactivated_lineages, continuing_lineages

