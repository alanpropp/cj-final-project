from operator import itemgetter
import csv
from os.path import join
BASE = 'Data'

def get_data(filename):
    with open(join(BASE, filename), 'r', encoding="latin1") as f:
        newrows = []
        for row in csv.DictReader(f):
            newrows.append(row)
        return newrows

def get_countries():
    FNAME = 'populationbycountrymillions.csv'
    rows = get_data(filename = FNAME)
    countries = []
    for row in rows:
        country = row[''] #The country column doesn't have a label - just blank
        countries.append(country)
    return countries

def years():
    years_list = []
    with open('templates/years.txt', 'r') as f:
        for line in f:
            years_list.append(line[0:4])
    return years_list

def get_correct_metric(metric):
    information = []
    if metric == 'coal':
        information = coal()
    elif metric == 'electricity':
        information = electricity_generation()
    elif metric == 'natural gas':
        information = natural_gas()
    elif metric == 'biofuels':
        information = biofuels()
    elif metric == 'energy':
        information = primary_energy_consumption()
    elif metric == 'renewable electricity':
        information = renewable_electricity_consumption()
    return information

def get_units(metric):
    units = ""
    if metric == 'coal':
        units = "quadrillion Btu"
    elif metric == 'electricity':
        units = 'billion kilowatt-hours'
    elif metric == 'natural gas':
        units = 'quadrillion Btu'
    elif metric == 'biofuels':
        units = 'thousand barrels per day'
    elif metric == 'energy':
        units = 'quadrillion Btu'
    elif metric == 'renewable electricity':
        units = 'billion kilowatt-hours'
    return units


def find_similar_countries(information, years_list, argument, country):
    similar_countries = [] #List of countries along with their relevant data points
    relevant_year = ""
    counter = len(argument)-1
    while counter>0:
        if argument[counter]!=None:
            relevant_year = years_list[counter]
            break
        counter-=1
    if counter!=0:
        country_data_point = float(argument[counter])
        for i in information:
            curr_country = i['']
            data_point = i[relevant_year]
            if data_point != 'NA' and data_point != '--' and curr_country != country:
                absolute = abs(country_data_point-float(data_point))
                entry = []
                entry.append(curr_country)
                entry.append(absolute)
                entry.append(float(data_point))
                similar_countries.append(entry)
            similar_countries = sorted(similar_countries, key = itemgetter(1))
    return similar_countries[0:10]

def percentage_total(information, years_list, argument):
    counter = len(argument)-1
    relevant_year = ""
    world_total = ""
    percentage = 0
    while counter>0:
        if argument[counter]!=None:
            relevant_year = years_list[counter]
            break

    for i in information:
        if i['']=='World':
            world_total = i[relevant_year]
            percentage = 100*float(argument[counter])/float(world_total)
            break
    return percentage



def natural_gas():
    FNAME = 'drynaturalgasconsumption.csv'
    return get_data(filename = FNAME)

def biofuels():
    FNAME = 'totalbiofuelsproduction.csv'
    return get_data(filename = FNAME)

def population():
    FNAME = 'populationbycountrymillions.csv'
    return get_data(filename = FNAME)

def coal():
    FNAME = 'totalcoalconsumption.csv'
    return get_data(filename = FNAME)

def electricity_generation():
    FNAME = 'totalelectricitynetgeneration.csv'
    return get_data(filename = FNAME)

def primary_energy_consumption():
    FNAME = 'totalprimaryenergyconsumption.csv'
    return get_data(filename = FNAME)

def renewable_electricity_consumption():
    FNAME = 'totalrenewableelectricitynetconsumption.csv'
    return get_data(filename = FNAME)
