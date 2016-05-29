
#Concept and Documentation
##App name: Worldwide Energy Consumption
##Elevator Pitch
There is a lot of energy usage data in existence, and many creative ways to visualize it. This app would allow users to visualize their energy data mainly by comparison, filtering based on a variety of different ways and in different categories (oil, natural gas, energy consumption per capita, etc.). I hope to allow for interesting map-based visualization, although that will likely depend on how complex my abilities turn out to be.

##Inspirations and prior work
* [IEA's Energy Atlas](http://energyatlas.iea.org/?subject=-1920537974)
	* Very useful as it shows sizes of circles proportional to that country's energy usage on the map
	* Several different metrics users can select
	* Unfortunate that there's only one map for oil, one for coal, one fo natural gas, etc.
	* Good ranking system on the side, and year slider bar

* [REN21 Interactive map (renewable energy)](http://www.ren21.net/status-of-renewables/ren21-interactive-map/)
	* Difficult to move map without zooming in/out, and to return to map after seeing country profile
	* Good to be able to filter by Topic and/or Technology.
	* Extensive information on country if you click on it, including very good showing of data sources
	* Allows for data download

* [CAIT Climate Data explorer](http://cait.wri.org/historical/Country%20GHG%20Emissions?indicator[]=Total%20GHG%20Emissions%20Excluding%20Land-Use%20Change%20and%20Forestry&indicator[]=Total%20GHG%20Emissions%20Including%20Land-Use%20Change%20and%20Forestry&year[]=2012&sortIdx=NaN&chartType=geo)
	* Very confusing user interface - relatively overwhelming
	* Pop-up map is useful, as you can hover over countries and get their specific emissions number. Also shows in color how bad countries' emissions are
	* Don't like the chart on the same page as the map - crowded
	* Overhwelmingly large number of things you can see about a country and sort by
	* Graphical format is relatively useless
* [IEA's Sankey Diagram](http://www.iea.org/Sankey/index.html)
	* Cool, different way of visualizing each country's energy resource to its end use
	* Can select country by country
	* Moving through the timeline since 1973 is relatively slick and easy
	* No ability to filter and compare countries
	* Layered - but not all the layers work

#Data
##Data Sources
1. <Data.gov> has a variety of different energy data tables containing energy usage information stretching back up to around 35 years.
	1. First, we have [total international primary energy consumption](http://catalog.data.gov/dataset/eia-data-total-international-primary-energy-consumption-6c124) for nearly all countries since 1980 (with a few holes of course)
	2. In addition, I want to include [population data](http://catalog.data.gov/dataset/population-by-country-1980-2010-d0250_) so that users can look at and filter by energy usage per capita if they want to
	3. This website has plenty of energy data for specific sources, starting with [coal](http://catalog.data.gov/dataset/annual-coal-consumption-by-country-1980-2009-12cb0). This data covers coal consumption by country stretching back to 1980, listed in quadrillion btu.
	4. There is also listed [biofuels consumption](http://catalog.data.gov/dataset/biofuels-consumption-and-production-by-country-2000-2010-11ff9), the data for which is only from 2000-2010 given the recent nature of its usage, but which could still be useful
	5. I will incorporate [annual electricity generation](http://catalog.data.gov/dataset/annual-electricity-generation-1980-2009-dff2e) since 1980 as well for comparison's sake
	6. Just in case it's at all useful, I may include [renewable electricity net generation data](http://catalog.data.gov/dataset/annual-renewable-electricity-net-generation-by-country-1980-2009-0c7a4).
	7. Similar to coal consumption, there is also [natural gas production data](http://catalog.data.gov/dataset/natural-gas-consumption-by-country-1980-2009-792f5) that would be useful to compare 

##Data grouping
Data will be grouped and compiled/combined based on country. In a country summary, the user can see all energy information for the various different resources grouped, and compared to other countries of similar status in the world


##Categorical variable
*I am still unsure what my categorical variable will be - would love some advice on this one*

##Continuous variables
The countinuous variables will be energy consumption in a variety of different resource categories, as well as all the same information but per capita

#Filtering options
Users can filter in a variety of different ways. This includes: 
* Energy resource type (oil, natural gas, etc.)
* Per capita or gross consumption
* Sorting options - alphabetical, smallest-largest or vice versa, above a certain level of consumption, etc.


#Views and Routes
##Map
Hopefully I will have an interactive map, although I think this might be difficult to achieve

##Homepage select options
The homepage will allow users to select how they want to see their data, how they want to sort it, if they want to compare countries, etc.

##Table
Once users select their information, they will be directed to a table with all relevant information