# -*- coding: utf-8 -*-
"""
Created on Tue May  9 20:59:54 2023

@author: dkbow
"""
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import geopandas as gpd
import seaborn as sns

#%%


#Calling/ reading the file to do necessary computations
UB_info = pd.read_csv("project.csv")

UB_info = pd.read_excel("UB_data.xlsx")


#Getting the total number of males in the program
num_males = UB_info['Sex'].value_counts()["M"]


#Getting the total number of females in the program
num_females = UB_info['Sex'].value_counts()["F"]


#Calculating the total number of students (male & female) in the program
total_students = len(UB_info.index)


#Sorting the number of students who are no longer participating in the program.
UB_students = UB_info.drop('hs_grad', inplace=False, axis=1)


#Adding up the total number of students participating in the program. 
stud_p = UB_students.eq("X").sum(axis=1).to_dict()


#Creating a dataframe with student participation per year in the program.
df = pd.DataFrame.from_dict(stud_p, orient ='index')
df = df.rename(columns = {0:'Number of Years in Program'}, inplace = False)



# Renaming the participation years to one year that will reflect
# the entrance of each student per cohort. 

final = pd.concat([UB_students, df], axis=1)
final = final.rename(columns = {'P2015-2016':'P2015'}, inplace = False)
final = final.rename(columns = {'P2016-2017':'P2016'}, inplace = False)
final = final.rename(columns = {'P2017-2018':'P2017'}, inplace = False)
final = final.rename(columns = {'P2018-2019':'P2018'}, inplace = False)
final = final.rename(columns = {'P2019-2020':'P2019'}, inplace = False)
final = final.rename(columns = {'P2020-2021':'P2020'}, inplace = False)
final = final.rename(columns = {'P2021-2022':'P2021'}, inplace = False)
#print(final)

#%%

#Looking at which zip codes most students in the program reside.




#Figuring out which zip codes female participants live

#This code is separating the male pupils from their female counterparts. 



female_final = final[final.Sex != "M"]
female_final = female_final['zip'].value_counts().reset_index().set_axis(
                    ['Zip','The Total Number of Female Students'], axis=1)

print("\n Total Number of Females Per Zip Code")
print(female_final)




#Figuring out which zip codes male participants live

#This code is separating the male pupils from their female counterparts. 
male_final = final[final.Sex != "F"]
male_final = male_final['zip'].value_counts().reset_index().set_axis(['Zip',
                                'The Total Number of Male Students'], axis=1)

print("\n Total Number of Males Per Zip Code")
print(male_final)
male_final.plot.scatter(x = 'Zip', y = 'The Total Number of Male Students', 
                        s = 100)


#Combining male and female students to see the aggregated total of pupils 
#per zip code. 

zip_gender = pd.merge(male_final, female_final, on='Zip', how = 'left')
zip_gender = zip_gender.fillna(0)
print("\n Total Students Per Zip Code")
print(zip_gender)


#Reading in the Zip Code CSV

syr_zips = gpd.read_file("Onondaga_zips.gpkg")


#Merging students' home zip code on zip codes in Onondaga County

zip_gender["Zip"] = zip_gender["Zip"].astype(str)


gender_zips = syr_zips.merge(zip_gender, left_on = "ZCTA5CE20", 
                          right_on= "Zip",
                          validate = "1:1",
                          how="outer",
                          indicator=True)

gender_zips["The Total Number of Male Students"].fillna(0,inplace=True)

gender_zips["The Total Number of Female Students"].fillna(0,inplace=True)

gender_zips.drop(columns=["Zip","_merge"],inplace=True)


gender_zips.to_file("Student_zips.gpkg",layer="students")








