# New Delhi House Rent Prediction: 

## Table of Content
  * [Overview](#overview)
  * [Approach towards end-to-end solution](#Approach towards end-to-end solution)
  * [Directory Tree](#directory-tree)
  * [Future scope of project](#future-scope)

## Overview
This is end-to-end New Delhi house price prediction machine learning project with Flask web app which predicts rent of house.
Data has collected from Kaggle https://www.kaggle.com/andynath/new-delhi-rental-listings

####Context
The dataset is from a rental price prediction project I did. Includes different types of properties (Apartments, Independent floors, Independent houses, Villas etc.)
It contains 17890 rental listings from a popular real estate website. It can be used for rental prediction projects, analysis of areas of affluence etc.

####Content
The dataset multiple quantitative, categorical and co-ordinate features including :

#####Data about the houses :
sizesqft,
propertyType,
bedrooms,

#####Data about the locality of the house :
latitude,
longitude,
localityName,
suburbName,
cityName,

#####Asking Rent :
price,

#####Property agency :
companyName,

#####Distance to closest landmarks : (geodesic distance, not driving-road distance)
closestmterostationkm, APdistkm, Aiimsdistkm, NDRLWdist_km

## Approach towards end-to-end solution
#### To do an end-to-end Machine Learning project we need to do the following steps

1. Understand the requirements of the business.
2. Acquire the dataset.
3. Visualize the data to understand it better and develop our intuition.
4. Pre-process the data to make it ready to feed to our ML model.
5. Try various models and train them. Select one that we find best.
7. Present your solution to the team.
8. Deploy on production environment.

## Directory Tree 
```
├── Data 
│   ├── New Delhi Rental List.csv
├── Jupyter notebook
│   ├── NewDelhi_Rent_Prediction_Model.ipynb
├── templates 
│   ├── home.html
├── .gitignore
├── NewDelhiRentPrice_model.pkl
├── New_Delhi.jpg
├── app.py
├── README.md
├── requirements.txt
```

## Future Scope

* Use multiple Algorithms
* Optimize Flask app.py
* Front-End on production