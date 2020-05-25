
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
            travel = toks[3]
            name = toks[1]
          
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
            
            tax_name = toks[1]
            country = toks[2]
            date = toks[4]
            epiweek = toks[5]
            lin_string = toks[6]

            metadata = [country, date, epiweek]
            
            new_taxon = classes.taxon(tax_name, lin_string, metadata)
            taxa.append(new_taxon)
            if new_taxon.date_dt != "NA":
                tax_with_dates.append(new_taxon)

            tax_dict[tax_name] = new_taxon
            
            lineages_to_taxa[lin_string].append(new_taxon)


    current_date = sorted(tax_with_dates, key=sortkey2, reverse = True)[0].date_dt
    #current_week = Week.fromdate(current_date)
    
    for lin, lin_specific_taxa in lineages_to_taxa.items():
        l_o = classes.lineage(lin, lin_specific_taxa, current_date)

        lin_obj_dict[lin] = l_o


    lin_obj_dict = parse_travel_history(lin_obj_dict, tax_dict, metadata_file)

    return lin_obj_dict, taxa, current_date

def get_recall_value(lin_obj_dict, recall_file):

    recall_dict = {}

    with open(recall_file) as f:
        next(f)
        for l in f:
            toks = l.strip("\n").split(",")
            name = toks[0]
            recall_value = toks[4]

            recall_dict[name] = recall_value

    for key, value in lin_obj_dict.items():
        value.recall_value = recall_dict[key]

    return lin_obj_dict


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
        dataframe_dict["Recall value"].append(i.recall_value)

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

    dataframe['Lineage name'] = pd.Categorical(dataframe['Lineage name'],categories=['A', 'A.1', 'A.1.1', '*A.1.2', 'A.1.3', 'A.2', 'A.3', 'A.4', 'A.5', 'A.6', 'A.p7', 'B', 'B.1', 'B.1.45', 'B.1.49', 'B.1.1', 'B.1.1.1', 'B.1.1.2', 'B.1.1.3', 'B.1.1.4', 'B.1.1.5', 'B.1.1.6', 'B.1.1.7', 'B.1.1.8', 'B.1.1.9', 'B.1.1.10', 'B.1.1.p11', 'B.1.1.p12', 'B.1.1.13', 'B.1.1.14', 'B.1.1.p15', 'B.1.1.p16', 'B.1.1.17', 'B.1.1.18', 'B.1.1.p19', 'B.1.p2', 'B.1.3', 'B.1.5', 'B.1.5.1', 'B.1.5.2', 'B.1.5.3', 'B.1.5.4', 'B.1.5.5', 'B.1.5.6', 'B.1.6', '*B.1.7', 'B.1.8', 'B.1.p9', 'B.1.p11', 'B.1.12', 'B.1.13', 'B.1.p16', 'B.1.19', '*B.1.20', 'B.1.p21', 'B.1.22', 'B.1.23', 'B.1.p25', 'B.1.26', 'B.1.27', '*B.1.28', 'B.1.29', 'B.1.30', 'B.1.31', 'B.1.32', 'B.1.33', 'B.1.34', 'B.1.35', 'B.1.36', 'B.1.37', 'B.1.38', 'B.1.39', 'B.1.40', 'B.1.41', 'B.1.p42', 'B.1.43', 'B.1.44', '*B.1.47', '*B.1.48', '*B.1.51', '*B.1.52', 'B.1.64', 'B.1.66', 'B.1.67', 'B.1.p68', 'B.1.69', 'B.1.70', 'B.1.71', 'B.1.72', 'B.1.p73', 'B.2', 'B.2.1', 'B.2.2', '*B.2.3', 'B.2.4', 'B.2.5', 'B.2.6', 'B.2.7', 'B.3', 'B.4', 'B.5', 'B.6', 'B.7', '*B.8', 'B.9', 'B.10', 'B.p11', 'B.p12', 'B.13', 'B.14', 'B.15', 'B.16'],ordered=True)
    dataframe.sort_values('Lineage name',ascending=True, inplace=True)
    # dataframe.sort_values(by=["Lineage name"], ascending=True, inplace=True)

    with_links = []
    for i in dataframe["Lineage name"]:
        name_plus_link = "[" + i + "]" + "(#" + i + ")"
        with_links.append(name_plus_link)
    dataframe["Lineage name"] = with_links

   
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

