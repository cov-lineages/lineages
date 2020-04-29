from epiweeks import Week, Year
import datetime as dt

def make_epiweeks():

    weeks = list(Year(2019).iterweeks())
    weeks.extend(list(Year(2020).iterweeks()))

    return weeks    

def make_current_week(week):

	bits = week.split("-")
	date = dt.date(int(bits[0]), int(bits[1]), int(bits[2]))
	#Add error if the date format isn't right

	return date

