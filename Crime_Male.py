# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:02:22 2023

@author: dkbow
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import geopandas as gpd
import seaborn as sns
import geopy


#%%

plt.rcParams["figure.dpi"] = 300


crime_2018 = gpd.read_file("Crime_Data_2018_-_Part_1_Offenses_(With_Lat_%26_Long_Info).zip")
crime_2018["ADDRESS"] = crime_2018["ADDRESS"] + ", Syracuse, NY"

crime_2018['lon'] = crime_2018['geometry'].x
crime_2018['lat'] = crime_2018['geometry'].y
crime_2018 = crime_2018.dropna()
print(crime_2018)


#Calling/ reading the file to do necessary computations
UB_info = pd.read_csv("project.csv")

UB_info = pd.read_excel("UB_data.xlsx")

#Sorting the number of students who are no longer participating in the program.
UB_students = UB_info.drop('hs_grad', inplace=False, axis=1)

#Adding up the total number of students participating in the program. 
stud_p = UB_students.eq("X").sum(axis=1).to_dict()


#Creating a dataframe with student participation per year in the program.
df = pd.DataFrame.from_dict(stud_p, orient ='index')
df = df.rename(columns = {0:'Number of Years in Program'}, inplace = False)


final = pd.concat([UB_students, df], axis=1)
final = final.rename(columns = {'P2015-2016':'P2015'}, inplace = False)
final = final.rename(columns = {'P2016-2017':'P2016'}, inplace = False)
final = final.rename(columns = {'P2017-2018':'P2017'}, inplace = False)
final = final.rename(columns = {'P2018-2019':'P2018'}, inplace = False)
final = final.rename(columns = {'P2019-2020':'P2019'}, inplace = False)
final = final.rename(columns = {'P2020-2021':'P2020'}, inplace = False)
final = final.rename(columns = {'P2021-2022':'P2021'}, inplace = False)


#%%

# Since the shapefile does not have any zipcodes, this section is retrieving
# the zipcodes for the addresses that crimes offered.


def get_zipcode(df, geolocator, lat_field, lon_field):
    location = geolocator.reverse((df[lat_field], df[lon_field]))
    return location.raw['address']['postcode']


geolocator = geopy.Nominatim(user_agent='username')

crime_2018['Zip_Code'] = crime_2018.apply(get_zipcode, axis=1,
                    geolocator=geolocator, lat_field='lat', lon_field='lon')

print("\n Address Zip Codes")
print(crime_2018)


#%%

# In this section, I will be creating a scatterplot to see if there is any
# correlation between male participation and crime rates. 



#crime.columns = ["Crime Type", "Number of Crimes Committed"]
crime = crime_2018["Zip_Code"].value_counts().rename_axis('zip').reset_index(name='Number of Crimes Committed')
print(crime)

male_final = final[final.Sex != "F"]
male_final = male_final['zip'].value_counts().reset_index().set_axis(['zip',
                                'The Total Number of Male Students'], axis=1)


print("\n Total Number of Males Per Zip Code")
print(male_final)

crime['zip'] = crime['zip'].astype('int64')
male_final['zip'] = male_final['zip'].astype('int64')

crime_male = pd.merge(crime, male_final, on='zip', how='outer')

crime_male = crime_male.dropna()
print(crime_male)

#crime_male.plot.scatter(x = 'zip', y ='Number of Crimes Committed', s = 100)
#crime_male.plot.scatter(x = 'zip', y ="The Total Number of Male Students", 
# s = 100)


# Creating a scatterplot to see if there is any relationship between the number
# of crimes committed and the total number of male students.

fig,ax=plt.subplots()

crime_male.plot.scatter(x="Number of Crimes Committed",
                y = "The Total Number of Male Students",ax=ax)
ax.set_title("Male_Participation_vs_Crime_Rates")
fig.tight_layout()
fig.savefig("Male_Participation_vs_Crime_Rates.png")



# Creating a regression to see if there is any statisitical significance

fig,ax=plt.subplots()

sns.regplot(data=crime_male,x ="Number of Crimes Committed",
                y = "The Total Number of Male Students",ax=ax)
ax.set_title("Male_crime_regression")
fig.tight_layout()
fig.savefig("Male_crime_regression.png")




#%%



