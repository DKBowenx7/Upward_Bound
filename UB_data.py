# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 00:47:03 2023

@author: dkbow
"""


import requests
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%%


#Reading Upward Program Student Participation Data
UB_info = pd.read_csv("UB_data.csv")
print(UB_info)


#%%
#Calculating the number of students in the program
#Deriving the total number of students by sex

print(UB_info["Sex"].value_counts())

num_males = UB_info["Sex"].value_counts()["M"]

num_females = UB_info["Sex"].value_counts()["F"]

total_students = len(UB_info.index)


#%%
#Percentage of Male and Female in the Program 


#Male %

percent_males = num_males / total_students

print("\n Percentage of Males in the Upward Bound")
print(percent_males)



#Female %

percent_females = num_females / total_students

print("\n Percentage of Females in the Upward Bound Program")
print(percent_females)


#%%

# In this section, I will be calculating the retention rate of females vs
# males in the Upward Bound Program

P_years = ["P2015-2016","P2016-2017","P2017-2018", "P2018-2019","P2019-2020",
           "P2020-2021", "P2021-2022"]



# Dropping the high school graduation (hs_grad) column to calculate 
# the retention rate before graduating 

UB_students = UB_info.drop("hs_grad", inplace=False, axis=1)
print(UB_students)



# Aggregating the students' participation (stud_p) in the Upward Bound Program 
# represented by X

stud_p = UB_students.eq("X").sum(axis=1).to_dict()

df = pd.DataFrame.from_dict(stud_p, orient = "index")


#Renaming the column, so it is easier to identify and read

df = df.rename(columns = {0: "Years of Participation in the Upward Bound Program"},
               inplace = False)

print(df)



#Attaching the results to the original information

final = pd.concat([UB_students, df], axis = 1)
print(final)

#%%

#Grouping how many students are in each zip code

group_zip = UB_info["zip"].value_counts()

print("\n Number of Students Per Zip Code")
print(group_zip)


#Breaking down the sexes per zipcode in the Upward Bound



#1st: Sorting the data to show only females per zip code by obmitting males

female_final = final[final.Sex != "M"]
female_final = female_final["zip"].value_counts().reset_index().set_axis(['Zip',
                                        'Number of Female Students'], axis=1)

print("\n Students Who Are Females Living In Each Zip Code")
print(female_final)




#2nd: Sorting the data to show only males per zip code by obmitting females

male_final = final[final.Sex != "F"]
male_final = male_final['zip'].value_counts().reset_index().set_axis(['Zip',
                                        'Number of Male Students'], axis=1)

print("\n Students Who Are Males Living In Each Zip Code")
print(male_final)


#%%

#Creating a bar graph to illustrate females and males, who are in the program 
# per zip code


zip_gender = pd.merge(male_final, female_final, on='Zip', how = 'left')
zip_gender = zip_gender.fillna(0)
print(zip_gender)

zip_gender.plot(x="Zip", y=["Number of Male Students", 
            "Number of Female Students"], kind="bar", figsize=(10, 9))

plt.xlabel("Students'Home Zip Code")
plt.ylabel("Male vs Females")
plt.title("Upward Bound Students' Per Home Zip Code")
plt.savefig("Students_Per_Zip_Code.png")
plt.show()


#%%
#Calculating students who dropped the program


#Students who dropped from the program focusing on year 2020
#Also, noting discontinued and moved as dropped


#how many students dropped out of program total & then male vs female

print(final["P2020-2021"].value_counts()["Discontinued"] + 
      final["P2020-2021"].value_counts()["Moved"])

final = final.rename(columns = {'P2020-2021':'P2020'}, inplace = False)
final.to_csv('students_dropped.csv')


gender_status = final.drop(final.columns[[0, 4, 5, 6, 7, 8, 10]],
                           axis=1, inplace=False)

gender_status.loc[gender_status["P2020"] == "Moved", "P2020"] = "Discontinued"



#Seeing how many females have dropped from the program, especially
#  with the focus on year 2020

female_only = gender_status[gender_status.Sex != "M"]

female_only = female_only['P2020'].value_counts().reset_index().set_axis(['P2020',
                                        'Number of Female Students'], axis=1)


print("\n Upward Bound Student Status")
print(female_only)



#Seeing how many males have dropped from the program, especially with the 
# focus on year 2020

male_only = gender_status[gender_status.Sex != "F"]

male_only = male_only['P2020'].value_counts().reset_index().set_axis(['P2020',
                                        'Number of Male Students'], axis=1)


print("\n Upward Bound Male Students Status")
print(male_only)


#true_dropped = true_dropped.rename(columns = {'P2020':'P2020-2021'}, 
# inplace = False)
#Now merging the results 

true_dropped = pd.merge(male_only, female_only, on='P2020', how = 'left')

print("\n Upward Bound Female Students Status")
print(true_dropped)



# Creating visualizations of the results

true_dropped.plot(x="P2020", y=["Number of Male Students", 
                "Number of Female Students"], kind="bar", figsize=(10, 9))
plt.xlabel("Participation Year 2020-2021")
plt.ylabel("Number of Males vs Females In The Program")
plt.title("Male vs Female Status In The Program")
plt.savefig("Male_vs_Female_Status.png")
plt.show()

#%%


















