# 2. Identify the data sources

Date Created: May 17, 2023 1:17 AM
Status: Task01

## Data Collection

1. Data needed on priority basis:
    - [x]  Collect address of public farms [***] >> Set the granular level to county and Texas!!
    - [x]  Use GeoCoding to find coordinates[***]
    - [x]  **Design an excel or python tool to calculate the emissions from farms [Brainstorm the parameters needed for this]**
    - [x]  Gather crop area
    - [x]  Obtain crop information
    - [x]  Collect emission data/ estimate
    - [x]  Gather land tillage information[?] - SOC is indirect contributor

There are more than 2 million farms in US. We cant collect data for each and every farm. 

For more generalist approach- we can collect data for 10 or 20  farms evenly placed in each state. - Later we can think about how we can scale the model

| Title | Link | Description |
| --- | --- | --- |
| USDA Census | https://www.nass.usda.gov/Quick_Stats/CDQT/chapter/2/table/8/year/2017 | Land Usage pattern |
| GHG Emission Data | https://cfpub.epa.gov/ghgdata/inventoryexplorer/#agriculture/entiresector/allgas/category/all | Agriculture specific emission + State specific |
|  | https://www.ceaconsulting.com/wp-content/uploads/greenhouse-gas-emissions-and-nitrogen-pollution-in-us-agriculture.pdf | Information to understand the context of emissions |
| Agriculture in US | https://en.wikipedia.org/wiki/Agriculture_in_the_United_States | Broad overview of Agriculture sector in US |
| Quantifying GHG emissions in Agriculture | https://www.usda.gov/sites/default/files/documents/USDATB1939_07072014.pdf |  |
| AUS GHG accounting tool | https://piccc.org.au/resources/Tools.html | just for reference |
| Low priority links | https://aditya-grover.github.io/blog/2023/climate-learn/ | ML library developed by students at intersection of AI and Climatechange |
| GHG emissions | https://data.nal.usda.gov/dataset/data-chapter-3-cropland-agriculture-us-agriculture-and-forestry-greenhouse-gas-inventory-1990-2018 |  |

> In the [United States](https://en.wikipedia.org/wiki/United_States), agriculture is the second largest emitter of [greenhouse gases](https://en.wikipedia.org/wiki/Greenhouse_gas) (GHG), behind the energy sector.[[66]](https://en.wikipedia.org/wiki/Agriculture_in_the_United_States#cite_note-Climate_change_and_agriculture_in_the_United_States_:02-66) Direct GHG emissions from the agricultural sector account for 8.4% of total U.S. emissions, but the loss of [soil organic carbon](https://en.wikipedia.org/wiki/Soil_carbon) through soil erosion indirectly contributes to emissions as well
> 

References:

1. [https://ourworldindata.org/food-ghg-emissions](https://ourworldindata.org/food-ghg-emissions)
2. [https://www.epa.gov/system/files/documents/2023-04/US-GHG-Inventory-2023-Main-Text.pdf](https://www.epa.gov/system/files/documents/2023-04/US-GHG-Inventory-2023-Main-Text.pdf)
3. [https://towardsdatascience.com/leveraging-geolocation-data-for-machine-learning-essential-techniques-192ce3a969bc](https://towardsdatascience.com/leveraging-geolocation-data-for-machine-learning-essential-techniques-192ce3a969bc)
4. [https://www.ceaconsulting.com/wp-content/uploads/greenhouse-gas-emissions-and-nitrogen-pollution-in-us-agriculture.pdf](https://www.ceaconsulting.com/wp-content/uploads/greenhouse-gas-emissions-and-nitrogen-pollution-in-us-agriculture.pdf)
5. [https://www.ipcc.ch/site/assets/uploads/2018/02/ar4-wg3-chapter8-1.pdf](https://www.ipcc.ch/site/assets/uploads/2018/02/ar4-wg3-chapter8-1.pdf)
6. [https://cfpub.epa.gov/ghgdata/inventoryexplorer/#agriculture/entiresector/allgas/category/all](https://cfpub.epa.gov/ghgdata/inventoryexplorer/#agriculture/entiresector/allgas/category/all)

Shape files? Which crops? Land use pattern? Technology? 

**Gathering data is a big challenge!**

## 

1. **Farming.**  Fortunately, [New Holland has an online calculator](https://agriculture.newholland.com/eu/en-uk/about-us/new-holland/clean-energy-leader/sustainable-farming/carbonid-calculator) that allows you to roughly estimate CO2 emissions from its tractor. For example, a modern 300 horsepower Tier 4 tractor operated for 200 hour per year would generate 51,950 lbs of CO2 per year. In metric tonnes, that equals 23.5 tonnes per year. (An older pre-DEF tractor can be calculated on the website too, and not surprisingly, is much worse). A farmer with the modern 300 hp tractor could offset his or her emissions by purchasing 23.5 carbon credits for $179.06 (at today’s price).