import datetime as dt
from collections import Counter
from collections import defaultdict
from epiweeks import Week,Year

class taxon():
    
    def __init__(self, record_id, lineage, metadata):
    
        self.id = record_id
        self.lineage = lineage
        
        self.country = metadata[0]
        self.date = metadata[1]

        epiweek_prep = metadata[2]
        if epiweek_prep != "":
            if float(epiweek_prep) != 0.0:
                self.epiweek = Week(2020, int(float(epiweek_prep)))
            else:
                self.epiweek = Week(2019, 52)
        else:
            self.epiweek = "NA"

        self.get_date_loc()

        self.travel_history = False
        
        
    def get_date_loc(self):
        
        date_bits = self.date.split("-")

        if len(date_bits) == 3:
            self.date_dt = dt.date(int(date_bits[0]), int(date_bits[1]), int(date_bits[2]))
        else:
            self.date_dt = "NA"

class lineage():
    
    def __init__(self, name, taxa, current_day):
        
        self.id = name
        
        if self.id == "":
            self.new = True
        else:
            self.new = False

        self.taxa = taxa
        
        self.dates = []
        self.epiweeks = []
        
        self.locations = []
        self.main_locs = []
        self.mains_plus_freqs = []

        self.country_freqs = {}
        
        self.get_date_loc_info(current_day)
        self.get_most_common_country()
        self.define_status(current_day)

        self.travel_history = defaultdict(set)
        
        
    def get_date_loc_info(self, current_day):
        
        for tax in self.taxa:
            if tax.date_dt != "NA":
                self.dates.append(tax.date_dt)
                self.locations.append(tax.country)
                self.epiweeks.append(tax.epiweek)

        self.date_counts = Counter(self.dates)
        self.loc_counts = Counter(self.locations)
        self.epiweek_counts = Counter(self.epiweeks)
                
        if self.dates == []:
            pass
        else:   
            self.mrd = max(self.dates)
            self.oldest = min(self.dates)
            
            self.pretty_mrd = self.mrd.strftime('%B %d')
            self.pretty_oldest = self.oldest.strftime('%B %d')

            self.length = (self.mrd - self.oldest).days
            
        self.last_sampled = (current_day - self.mrd).days

        
    def get_most_common_country(self):
        
        total = len(self.taxa)
        
        for country, count in self.loc_counts.items():
            
            frequency = count/total
            
            self.country_freqs[country] = count/total
            
        all_3 = self.loc_counts.most_common(3)
        self.main_locs = [i[0] for i in all_3]

        for i in self.main_locs:
            freq = self.country_freqs[i]
            pretty_freq = "(" + str(round(freq*100)) + "%)"
            
            self.mains_plus_freqs.append((i + " " + pretty_freq))


    def define_status(self, current_date): 

        if self.last_sampled < 7:
            for tax in self.taxa:
                date_diff = (current_date - tax.date_dt).days
                if date_diff > 7 and date_diff < 14:
                    self.status = "Continuing"
                    break
                else:
                    self.status = "Reactivated"
            
        elif self.last_sampled >= 7 and self.last_sampled < 14:
            self.status = "Gone quiet" 
        elif self.last_sampled >= 14 and self.last_sampled < 28:
            self.status = "Pending extinction"
        elif self.last_sampled >=28:
            self.status="Extinct"

        if not self.status:
            print("failed to assign status to " + self.name) 

        