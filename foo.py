from helpers import get_countries
from operator import itemgetter

#from helpers import filter_by_debt, filter_by_cost, filter_by_earnings, sort_by_criteria


# store the datarows in memory
countries = get_countries()

# # this function is the only one that app.py needs to know about
# def just_do_it(current = ""):
#     datarows = schools
#     if current == "smallest":
#         filteredrows = filter_by_smallest(datarows =schools)
#     elif current == "middle":
#         filteredrows = filter_by_middle(datarows =schools)
#     elif current == "largest":
#         filteredrows = filter_by_largest(datarows = schools)
#     # then, sort and return the result
#     # remember to pass in filteredrows
#     filteredrows = sorted(filteredrows, key = lambda elem: int(elem['NPT4_PUB']))
#  #   filteredrows = sorted(filteredrows, key = itemgetter('NPT4_PUB'))
#     return filteredrows