# 1. Understanding the Problem

Date Created: May 17, 2023 1:17 AM
Status: Task01

![Untitled](1%20Understanding%20the%20Problem%20c63a9af19b324abfaba945b9e1a11480/Untitled.png)

## Issue Identification:

- Crop generated GHG emissions
- We are talking about 27% of 26% ~~~~ approx 7% emission are through crop production + If we include land use then accounts to 14%(aprox)

![Untitled](1%20Understanding%20the%20Problem%20c63a9af19b324abfaba945b9e1a11480/Untitled%201.png)

![Untitled](1%20Understanding%20the%20Problem%20c63a9af19b324abfaba945b9e1a11480/Untitled%202.png)

## **Parameters**:

1. Land Usage
2. Land Area
3. Existing emissions for the location
4. Farming type
5. Farming Technology 
6. Crops?
7. Latitude
8. Longitude

STEPS:

1. Design a tool preferably in excel to generate emissions for individual farms based on few parameters
2. Later use this data as input for the ML problem

## OUTPUT:

1. Emission Prediction

## OBJECTIVE:

1. Create a emission calculator:
    1. How
        
        $$
        F(lat, long) ----> emissions
        $$
        
        What other parameters does client want?
        

Questions:

1. Do we have to think about this problem spatially or in linear fashion.
    1. E.g. Crops: Rice and Corn> Largest Producers of GHGs
        1. Multiple linear Regression
    
    **It’s most likely Linear Regression Problem**
    
    1. e.g Lat and Log: Its clustering problem
        1. Where private farms will be my test dataset.
        
2. Big Challenge is how do I convert the lat and long data into numerical data!! for MLR if thats the algorithm
    1. [https://www.kaggle.com/code/camnugent/geospatial-feature-engineering-and-visualization/notebook](https://www.kaggle.com/code/camnugent/geospatial-feature-engineering-and-visualization/notebook)
    

1. Create a framework/ methodology to calculate the farm emissions based on Latitude and Longitudinal Data
2. Public Farm: Emission Data: Should we Generate it or Scrape it.?
3. If scrape from where?
4. Private Farm: Test Data: Do the predictions here
5. Clustering! is one algo we can use here. DT might also work. Will decide based on accuracy.
6. What should be good KPI’s?
7. JSON or Shape file for the Public farms is it available? or Do we need to create it? Geomapping will be a challenge. 
8. Computationally expensive exercise- if we are considering whole of US. Better select a state and work on it. Again- state is not a small space as well.🤔
9. Scalable model? 
10. Also, calculating emissions based on region VS calculating emissions based on crop. For example- corn, rice are major GHG producers. Should we include them in feature matrix? (Problem statement is more towards region based prediction)

We also need some information on below points:

1. In between 1991-2023: What is range of US emissions and sequestration? (if possible for individual gases)
2. Is this data being collected in real-time or do we have to rely on past historical data and do the forecasting/ predictions?
3. Given the Range: can we generate the data?
4. Mitigation and Adaptation opportunities?
5. Data on Emission Growth Rate?

> Non-food emissions have an alternative But, Food emissions does it have an alternative? are you willing to do diet change?
>