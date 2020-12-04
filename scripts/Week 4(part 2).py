#!/usr/bin/env python
# coding: utf-8

# # The battle of Neighborhoods
# 
# ## Week 4 : Part b) -
# 
# ### Title : Restaurant recommender system in Bangalore
# 
# #### Data requirements :
# 
# To find a solution to the questions and build a recommender model, we need data and lots of data. Data can answer question which are unimaginable and non answerable by humans because humans do not have the tendency to analyse such large dataset and produce analtics to find a solutions.
# 
# Let's consider the base scenario :
# 
# Suppose i want to find a restaurant, then logically, i need 3 things :
# 
# 1. Its geographical coordinates(latitide and longitude) to find our where exactly it is located.
# 2. Population of the neighborhood where the restaurant is located.
# 3. Average income of neighborhood to know how much is the restaurant worth.
# 
# Lets take a closer look at each of these :
# 
# 1. To access location of a restaurant, its Latitude and Longitude is to be known so that we can point at its coordinates and create a map displaying all the restaurants with its labels respectively.
# 2. Population of a neighborhood is very important factor in determining a restaurant's growth and amount of customers who turn up to eat. Logically, the more the population of a neighborhood, the more people will be interested to walk openly into a restaurant and less the population, less number of people frequently visit a restaurant. Also if more people visit, better the restaurant is rated because it is accessed by different people with different taste. Hence is is very important factor.
# 3. Income of a neighborhood is also very important factor as population was. Income is directly proportional to richness of a neighborhood. If people in a neighborhood earns more than an average income, then it is very much possible that they will spend more however not always true with very less probability. So an restaurant accessment is proportional to income of a neighborhood.
# 
# #### Data collection :
# Collecting geographical coordinates is not difficult but after googling for more than 2 days, it was not available on open source data websites such as wikipedia, india gov website, census report websites etc. So i decided to use Google maps API to fetch latitude and longitude but google API has limited number of calls that i could make with my free account. So it would take around 15 - 20 days to fetch location of all the neighborhoods in bangalore. Initially i scrapped list of neighbor's using beautifulSoup4 from wikipedia. The table headings becoming the boroughs and data becoming the neighborhoods. Bangalore has 8 boroghs and 64 neighborhoods. So i manually googled each neighborhood to find its corresponding latitude and longitude. After doing so, i produced the following dataframe.
# ![image.png](attachment:image.png)

# Population by neighborhood is again easy to find out given that its readily available. But incase of bangalore, it is again not the case. i was able to find population data for few cities. Here is the link. Rest other neighborhood population is assumed and may be inaccurate but since this is a demonstrating project, the main idea to get the working model. The dataframe for bangalore neighborhood population looks like :
# ![image.png](attachment:image.png)

# Income by neighborhood is again easy to find out given that its readily available. But incase of bangalore, it is again not the case. i was able to find Income data for main city. Here is the link. Neighborhood Income is assumed and may be inaccurate but since this is a demonstrating project, the main idea to get the working model. The dataframe for bangalore neighborhood population looks like :
# ![image.png](attachment:image.png)

# FourSquare API :
# Use of foursquare is focused to fetch nearest venue locations so that we can use them to form a cluster. Foursquare api leverages the power of finding nearest venues in a radius(in my case : 500mts) and also corresponding coordinates,venue location and names. After calling, the following dataframe is created:
# ![image.png](attachment:image.png)

# The following map is produced by marking all the neighborhoods in bangalore city:
# ![image.png](attachment:image.png)

# In[ ]:




