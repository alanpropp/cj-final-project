
#Concept and Documentation
##App name: LA Energy Atlas
##Elevator Pitch
Los Angeles is an enormous consumer of energy, making it a very interesting case study in breaking down how, why, and where energy is used. UCLA has helped to build a site called [LA Energy Atlas](http://www.energyatlas.ucla.edu/) that helps users visualize in a variety of different ways the usage of energy in the greater LA area.

##Inspirations and prior work
* [Georgia's Energy Data Visualizer](http://www.georgiaenergydata.org/electricityproduction)
..* Great visualization of complex energy production data using visually appealing icons and colors.
..* Good graph as well showing installed capacity.
..* However, the search bar isn't well explained and doesn't seem to work (?)

* [USGS Energy Vision](http://certmapper.cr.usgs.gov/data/energyvision/)
..* Customizable base map is useful, as is ability to add layers.
..* No way for user to search anything other than checkboxes, rendering any user curiosity useless.

#Data
##Data Sources
1. The data is from the various utilities in Los Angeles County, both IOU's and MOU's.
2. They also included geocoded or site-collected location coordinates including the North American Industrial Classifications (NAICS) and/or Standard Industrial Classifications (SIC), and information about rate tariffs and special program participation in the database when available
3. The building information is derived from the 2008 Los Angeles County Assessor’s parcel dataset.
4. They also used information from the US census for demographics and income-related analyses

##Data grouping
Data was grouped (in the map, at least) based on county, and could be filtered within those counties

##Categorical variable
In a county summary, the user can see consumption grouped by a variety of different categories, most commonly clumped by years (10 or 20 year spans), income level, and building size. 

##Continuous variable
The countinuous variable tends to be total consumption and consumption by specific sources

#Filtering options
Users can filter in a variety of different ways. This includes: 
* Building type (residential, commercial, industrial, institutional, etc.)
* Consumption type (combined, electricity, natural gas, greenhouse gas, etc.)
* Area (COG's, Cities, Neighborhoods)
* Metric (median parcel consumption, percentage of countywide consumption, etc.)

#Views and Routes
##Map
There is an interactive map where users can click on specific cities within LA County to open a pop-up window with more specifics. The map is layered with colors based on consumption
![image Map.png](assets/Map.png)
![image PopUp.png](assets/PopUp.png)


##Profile Directory
If the user opens a full profile summary of a specific area, they see a page with a variety of graphs and charts to see how that area uses energy by a variety of different metrics (all interactive)
![image Profile_Directory.png](https://github.com/alanpropp/cj-final-project/blob/master/Assets/Profile_Directory.png)


##Table
Same information as the map, but different visualization. Here, we can sort the county medians based on any metric you want, compare between county medians, AND see/compare multiple customizable information about specific county medians simultaneously. The data is downloadable from here as well
![image Table.png](assets/Table.png)
