from operator import itemgetter
import csv
from os.path import join
from collections import OrderedDict
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

def get_Ordered_Dict(diction):
    years_list = years()
    product = OrderedDict()
    for year in years_list:
        product[year] = diction[year]
    return product


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
