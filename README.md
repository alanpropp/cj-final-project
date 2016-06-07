
#Concept and Documentation
##App name: EnergyData: How is your country doing?
##Elevator Pitch
There is a lot of energy usage data in existence, and many creative ways to visualize it. This app would allow users to visualize their energy data mainly by comparison, filtering based on a variety of different ways and in different categories (oil, natural gas, energy consumption per capita, etc.). An important component of this is to not only visualize their usage, but also to compare it side by side with their per capita usage, in order to separate the increases in their usage from the increases in their population.

Psychology studies show that the most effective way to incite behavior change is to compare peoples' usage to their neighbors' usage. In this case, I would allow users to compare their nation's usage to any other nation, and see how that has changed over time. In addition, users would be able to filter by ranking nations in particular categories and by selecting a specific nation to see its usage in more detail. I hope to allow users to see how their nation and others have changed their usage in different categories over time, in order to better understand where they might be trending. Hopefully, this application will allow users to understand better how their country fits in the global context of energy usage, and see if they are using more than their share.

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
* [Our World in Data map](https://ourworldindata.org/roser/maps/EnergyConsumptioPerCapita/EnergyConsumptioPerCapita.html)
	* Interesting and very visual, color-coded
	* Very simplistic in terms of information given
	* I actually like limited options for decades - reduces complexity
	* Difficult to find source

#Data
##Data Sources
1. Data.gov has a variety of different energy data tables containing energy usage information stretching back up to around 35 years. All energy data is provided by the EIA's International Energy Statistics site.
	1. First, we have [total international primary energy consumption](http://catalog.data.gov/dataset/eia-data-total-international-primary-energy-consumption-6c124) for nearly all countries since 1980 (with a few holes of course)
	2. This website has plenty of energy data for specific sources, starting with [coal](http://catalog.data.gov/dataset/annual-coal-consumption-by-country-1980-2009-12cb0). This data covers coal consumption by country stretching back to 1980, listed in quadrillion btu.
	3. There is also listed [biofuels consumption](http://catalog.data.gov/dataset/biofuels-consumption-and-production-by-country-2000-2010-11ff9), the data for which is only from 2000-2010 given the recent nature of its usage, but which could still be useful
	4. I will incorporate [annual electricity generation](http://catalog.data.gov/dataset/annual-electricity-generation-1980-2009-dff2e) since 1980 as well for comparison's sake
	5. Just in case it's at all useful, I may include [renewable electricity net generation data](http://catalog.data.gov/dataset/annual-renewable-electricity-net-generation-by-country-1980-2009-0c7a4).
	6. Similar to coal consumption, there is also [natural gas production data](http://catalog.data.gov/dataset/natural-gas-consumption-by-country-1980-2009-792f5) that would be useful to compare 
2. 	In addition, I want to include [population data](http://catalog.data.gov/dataset/population-by-country-1980-2010-d0250_) so that users can look at and filter by energy usage per capita if they want to. This data is provided by Data.gov but comes from the US Census Bureau. This data will be joined with the energy data, matched by country name

##Data grouping
Data will be grouped and compiled/combined based on country. In a country summary, the user can see all energy information for the various different resources grouped, and compared to other countries of similar status in the world


##Categorical variable
Category-specific percentage of the world vs. population percentage

##Continuous variables
The countinuous variables will be energy consumption in a variety of different resource categories, as well as all the same information but per capita

##Fun facts
The page will contain a link to a page with fun facts about the country - such as history, summary, etc. - assuming the country is a major nation and has its own site

#Filtering options
Users can filter in a variety of different ways. This includes: 
* Country
* Energy resource type (oil, natural gas, etc.)
* Sorting options - alphabetical, smallest-largest or vice versa, above a certain level of consumption, etc.
* Compared to other countries - pick two countries and compare them


#Views and Routes

##Homepage select options
The homepage will allow users to select what particular country or region they would like to view data for, and what dataset they want to see for it. It will allow them too to just get a ranked list for one category specifically, or to compare two countries side by side (a critical category to allow comparison between nations)
![image Homepage.png](https://github.com/alanpropp/cj-final-project/blob/master/Assets/Homepage.png)

##Table
On the country-specific results page, viewers can see a table with the year-by-year info for that particular metric, that country's population, and the metric per capita.
![image Table2.png](https://github.com/alanpropp/cj-final-project/blob/master/Assets/Table2.png)


##Graphs
On the country-specific results page, viewers can see graphs of the country's usage of whatever the user selected, as well as a graph of that usage per capita. Also, on the comparing 2 countries pages, users can select two countries and compare them in overall and per capita usage
![image Overall_graph.png](https://github.com/alanpropp/cj-final-project/blob/master/Assets/Overall_graph.png)
![image Comparison.png](https://github.com/alanpropp/cj-final-project/blob/master/Assets/Comparison.png)


