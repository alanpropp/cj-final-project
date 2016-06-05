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
        #Remove countries with negligible population
        if row['2010']!='NA' and row['2009']!='NA' and row['2010']!='--' and row['2009']!='--':
            countries.append(country)
    return countries

def years():
    years_list = []
    with open('templates/years.txt', 'r') as f:
        for line in f:
            years_list.append(line[0:4])
    return years_list

def population_rank(country):
    countries = get_countries()
    population_data = population()
    mylist = []
    for p in population_data:
        if p['2010']!='NA' and p['2010']!='--':
            curr_list = []
            curr_list.append(p[''])
            curr_list.append(float(p['2010']))
            mylist.append(curr_list)
    mylist = sorted(mylist, key = itemgetter(1), reverse=True)
    for counter in range(0, len(mylist)):
        if mylist[counter][0] == country:
            return counter+1
    return None

def usage_rank_per_capita(country, information):
    population_data = population()
    #Create dictionary for country and population
    dictionary = {}
    for i in population_data:
        if i['2008']!='NA' and i['2008']!='--' and i['2008']!=None:
            dictionary[i['']] = float(i['2008'])
    countries = get_countries()    
    mylist = []
    for p in information:
        if p.get('2008'):
            if p['2008']!='NA' and p['2008']!='--':
                curr_list = []
                curr_list.append(p[''])
                if dictionary.get(p[''])!=0 and dictionary.get(p[''])!=None:
                    per_capita = float(p['2008'])/dictionary.get(p[''])
                    curr_list.append(per_capita)
                else:
                    curr_list.append(0)
                mylist.append(curr_list)
    mylist = sorted(mylist, key = itemgetter(1), reverse=True)
    for counter in range(0, len(mylist)):
        if mylist[counter][0] == country:
            return counter+1
    return None


def usage_rank(country, information):
    countries = get_countries()
    mylist = []
    for p in information:
        if p.get('2008'):
            if p['2008']!='NA' and p['2008']!='--':
                curr_list = []
                curr_list.append(p[''])
                curr_list.append(float(p['2008']))
                mylist.append(curr_list)
    mylist = sorted(mylist, key = itemgetter(1), reverse=True)
    for counter in range(0, len(mylist)):
        if mylist[counter][0] == country:
            return counter+1
    return None


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
    elif metric == 'primary energy':
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
    elif metric == 'primary energy':
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

def percentage_energy(information, years_list, argument):
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
    return round(percentage, 6)

def percentage_population(country):
    populations = population()
    country_pop = 0
    world_pop = 0
    for p in populations:
        if p[''] == country:
            country_pop=float(p['2010'])
        if p[''] == 'World':
            world_pop = float(p['2010'])
    return round(100*country_pop/world_pop, 6)


def ranked_list(information):
    result = []
    for i in information:
        if i.get('2008') and i['2008']!='NA' and i['2008']!='--':
            curr_list = []
            curr_list.append(i[''])
            curr_list.append(float(i['2008']))
            result.append(curr_list)
    result = sorted(result, key = itemgetter(1), reverse = True)
    return result

def get_fun_facts(country):
    country = country.lower()
    country = country.replace('&', 'and')
    country = country.replace('.', '')
    country = country.replace(',', '')
    country = country.replace(' ', '-')
    return 'http://www.factmonster.com/country/' + country + '.html'

def get_country_data(country, information):
    data = []
    for i in information:
        if i[''] == country:
            for year in years():
                if i.get(year):
                    if i[year] == 'NA' or i[year] == '--':
                        data.append(None)
                    else:
                        data.append(float(i[year]))
    return data

def get_years_list(information):
    years_list = []
    curr = information[0]
    for year in years():
        if curr.get(year):
            years_list.append(year)
    return years_list

def compare_per_capita(country, country_data, years):
    per_capita = []
    populations = population()
    counter = 0
    for p in populations:
        if p[''] == country:
            for year in years:
                curr_data_point = float(country_data[counter])
                per_capita.append(curr_data_point/float(p[year]))
                counter+=1
    return per_capita

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
