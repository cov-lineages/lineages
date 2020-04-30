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
    
    def __init__(self, name, taxa, current_day, current_week):
        
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
        self.define_status(current_week)

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


    def define_status(self, current_week): 

        last_week = current_week - 1
        two_weeks_ago = current_week - 2
        last_two_weeks = [current_week-1, current_week-2]
        last_month = [current_week-1, current_week-2, current_week-3, current_week-4]


        int_list = []
        for k,v in self.epiweek_counts.items():
            if k in last_month:
                int_list.append(v)
        
        if self.epiweek_counts[current_week] != 0:
            if self.epiweek_counts[last_week] == 0:
                self.status = "Reactivated"
                self.newly_active = True

                count_list = list(self.epiweek_counts.values())

                self.latency_time = next((i for i, x in enumerate(count_list[1:]) if x), None) #in weeks
            
            else:
                self.status = "Continuing"
                self.always_active = True          

        else:
            if (self.epiweek_counts[last_week] == 0 and self.epiweek_counts[two_weeks_ago] != 0) or self.epiweek_counts[last_week] != 0: #not this week or last week, but week before
                self.status = "Gone quiet"
                self.quiet = True
            elif all([v==0 for v in int_list]):
                self.status = "Extinct"
                self.extinct = True
            else:
                self.status = "Pending extinction"
                self.pending = True

    
        if not self.status:
            print("failed to assign status to " + self.name) 