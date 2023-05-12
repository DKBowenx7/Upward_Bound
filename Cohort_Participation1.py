# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:29:39 2023

@author: dkbow
"""
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

#%%
                         #The Goal of this Script

# In this script, I will be breaking down the aggregated data presented in 
# UB_info(information on Upward Bound Students)

# I will be separating the female students from the male pupils. 
# The goal is to show graphically the difference between male and female 
# participation in the program per cohort.


#%%


#Calling/ reading the file to do necessary computations
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


#Renaming the participation years to one year that will reflect the entrance 
# of each student per cohort. 

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

                      
     # The Section Focuses On the 2015 Cohort 

#Goal: This section will separate the females and the males in this cohort by 
# showing the percentages and status of each student
                             
#Creating a dataframe showing only the 2015 cohort


#Locating the cells that have n.a. that signalizes the unknown status of 
# the students in the 2015 cohort

P2015 = final.loc[final["P2015"] != "n_a"]

P2015 = P2015.replace("Moved", "Discontinued")
print("\n Showing the Status of the 2015 Cohort at the End of the Program")
print(P2015)


P2015F = P2015.drop(['P2016', 'P2017', 'P2018', 'P2019', 'P2020', 'P2021'], 
                    axis=1)
print("\n Students Entering the Program in 2015")
print(P2015F)

#Computing how many students entered in the program in 2015
P2015_total_students = len(P2015F.index)

#%%

#This section will be focusing primarily on female students in the 2015 cohort.
# FEMALES IN THE 2015 COHORT



#Deriving the total number of females in the 2015 cohort
female_P2015 = P2015F['Sex'].value_counts()["F"]
print("\n Amount of Females in the 2015 Cohorts")
print(female_P2015)


#Calculating what percentage of females

female_P2015_percentage = female_P2015 / P2015_total_students
print("\n Percentage of Females in the 2015 Cohorts")
print(female_P2015_percentage)


#Separating females in the program information. 
# So, only female data is shown throughout the year


female_f = P2015[P2015.Sex != "M"]
print("\n Female Only Data")
print(female_f)



#%%

#This section will be focusing primarily on male students in the 2015 cohort.
# MALES IN THE 2015 COHORT


#Deriving the total number of males in the 2015 cohort
male_P2015 = P2015F['Sex'].value_counts()["M"]
print(male_P2015)


#Calculating what percentage of males
male_P2015_percentage = male_P2015 / P2015_total_students
print("\n 2015 Cohort Male Percentages")
print(male_P2015_percentage)


#Separating males in the program information. 
# So, only male data is shown throughout the year

male_f = P2015[P2015.Sex != "F"]
print("\n Male Only Data ")
print(male_f)



#Creating a Pie Chart that Shows the Aggregate of Male and Females
P2015F.groupby(['Sex']).sum().plot(title="2015 Male vs Female in Program", 
            kind='pie', y='Number of Years in Program', autopct='%1.0f%%')
plt.savefig("2015 Gender vs Years in Program")


#%%

#The Section Above, Which Focuses on the 2015 Cohort is Finished!!


#%%

     # The Section Focuses on the 2016 Cohort 

#Goal: This section will separate the females and the males in this cohort 
# by showing the percentages and status of each student
                             
#Creating a dataframe showing only the 2016 cohort



#This will be showing the number of students entering the program
# during this year.

P2016 = final.loc[final["P2016"] != "n_a"]


test = P2016[~P2016.isin(P2015)]
print(test)

test = test.dropna()
P2016F = test.drop(['P2015', 'P2017', 'P2018', 'P2019', 'P2020', 'P2021'], 
                   axis=1)
print(P2016F)


#Calculating the total number of students in the program
P2016_totalstudents = len(P2016F.index)
print("\n The 2016 Total Student Attendance")
print(P2016_totalstudents)



#Identifying the females in the 2016 cohort
female_P2016 = P2016F['Sex'].value_counts()["F"]
print("\n Total Females in the 2016 Cohort")
print(female_P2016)



#Calculating what percentage of females
female_P2016_p = female_P2016 / P2016_totalstudents
print("\n 2016 Female Percentage")
print(female_P2016_p)



#Identifying the males in the 2016 cohort
male_P2016 = P2016F['Sex'].value_counts()["M"]
print("\n 2016 Male Count")
print(male_P2016)



#Calculating what percentage of males
male_P2016_percentage = male_P2016 / P2016_totalstudents
print("\n 2016 Male Percentage")
print(male_P2016_percentage)



#Creating a Pie Chart that Shows the Aggregate of Male and Females
P2016F.groupby(['Sex']).sum().plot(
    title="2016 Cohort Male vs Females in Program", kind='pie',
    y='Number of Years in Program', autopct='%1.0f%%')
plt.savefig("2016 Gender vs Years in Program")


#%%

#The Section Above, Which Focuses on the 2016 Cohort, is Finished!!


#%%

  # The Section Focuses on the 2017 Cohort 

#Goal: This section will separate the females and the males in this cohort 
# by showing the percentages and status of each student
                             
#Creating a dataframe showing only the 2017 cohort


#This will be showing the number of students entering 
# the program during this year

P2017 = final.loc[final["P2017"] != "n_a"]
test1 = P2017[~P2017.isin(P2016)]

test1 = test1.dropna()
P2017F = test1.drop(['P2015', 'P2016', 'P2018', 'P2019', 'P2020', 'P2021'], 
                    axis=1)


#Calculating the total number of students in the program
P2017_totalstudents = len(P2017F.index)
print("\n Total Number of Students in the 2017 Cohort")
print(P2017_totalstudents)


#Identifying the females in the 2017 cohort
female_P2017 = P2017F['Sex'].value_counts()["F"]
print("\n Cohort 2017 Females")
print(female_P2017)



#Calculating what percentage of females
female_P2017_percentage = female_P2017 / P2017_totalstudents
print("\n 2017 Female Percentage")
print(female_P2017_percentage)



#Identifying the males in the 2017 cohort
male_P2017 = P2017F['Sex'].value_counts()["M"]
print("\n 2017 Male Cohort Total")
print(male_P2017)



#Calculating what percentage of males
male_P2017_p = male_P2017 / P2017_totalstudents
print("2017 Male Percentage")
print(male_P2017_p)


#Creating a Pie Chart that Shows the Aggregate of Male and Females
P2017F.groupby(['Sex']).sum().plot(
    title="2017 Cohort Male vs Females in Program", kind='pie', 
    y='Number of Years in Program', autopct='%1.0f%%')
plt.savefig("2017 Cohort Male vs Females in Program")



#%%

#The Section Above, Which Focuses on the 2017 Cohort, is Finished!!


#%%

 # The Section Focuses on the 2018 Cohort 

#Goal: This section will separate the females and the males in this cohort 
# by showing the percentages and status of each student
                             
#Creating a dataframe showing only the 2018 cohort



#This will be showing the number of students entering
# the program during this year

P2018 = final.loc[final["P2018"] != "n_a"]
test2 = P2018[~P2018.isin(P2017)]

test2 = test2.dropna()
P2018F = test2.drop(['P2015', 'P2016', 'P2017', 'P2019', 'P2020', 'P2021'], 
                    axis=1)
print(P2018F)


#Calculating the total number of students in the program
P2018_totalstudents = len(P2018F.index)
print("\n The Total Number of Students in the 2018 Cohort")
print(P2018_totalstudents)


#Identifying the females in the 2018 cohort
female_P2018 = P2018F['Sex'].value_counts()["F"]
print("\n Cohort 2018 Females")
print(female_P2018)



#Calculating what percentage of females
female_P2018_percentage = female_P2018 / P2018_totalstudents
print("\n 2018 Female Percentage")
print(female_P2018_percentage)


#Identifying the males in the 2018 cohort
male_P2018 = P2018F['Sex'].value_counts()["M"]
print("\n 2018 Male Count")
print(male_P2018)


#Calculating what percentage of males
male_P2018_percentage = male_P2018 / P2018_totalstudents
print("\n 2018 Male Percentage")
print(male_P2018_percentage)


#Creating a Pie Chart that Shows the Aggregate of Male and Females
P2018F.groupby(['Sex']).sum().plot(
    title="2018 Cohort of Males vs Females in Program", kind='pie', 
    y='Number of Years in Program', autopct='%1.0f%%')
plt.savefig("2018 Cohort of Male vs Female in Program")

#%%

#The Section Above, Which Focuses on the 2018 Cohort, is Finished!!

#%%

# The Section Focuses on the 2019 Cohort 

#Goal: This section will separate the females and the males in this cohort
# by showing the percentages and status of each student
                             
#Creating a dataframe showing only the 2019 cohort



#This will be showing the number of students entering 
# the program during this year
P2019 = final.loc[final["P2019"] != "n_a"]
test2 = P2019[~P2019.isin(P2018)]

test2 = test2.dropna()
P2019F = test2.drop(['P2015', 'P2016', 'P2017', 'P2019', 'P2020', 'P2021'], 
                    axis=1)
print(P2019F)


#Calculating the total number of students in the program
P2019_totalstudents = len(P2019F.index)
print("\n The Total Number of Students in the 2019 Cohort")
print(P2019_totalstudents)


#Identifying the females in the 2019 cohort
female_P2019 = P2019F['Sex'].value_counts()["F"]
print("\n Cohort 2019 Females")
print(female_P2019)



#Calculating what percentage of females
female_P2019_percentage = female_P2019 / P2019_totalstudents
print("\n 2019 Female Percentage")
print(female_P2019_percentage)


#Identifying the males in the 2019 cohort
male_P2019 = P2019F['Sex'].value_counts()["M"]
print("\n 2019 Male Count")
print(male_P2019)


#Calculating what percentage of males
male_P2019_percentage = male_P2019 / P2019_totalstudents
print("\n 2019 Male Percentage")
print(male_P2019_percentage)


#Creating a Pie Chart that Shows the Aggregate of Male and Females
P2018F.groupby(['Sex']).sum().plot(
    title="2019 Cohort of Males vs Females in Program", kind='pie', 
    y='Number of Years in Program', autopct='%1.0f%%')
plt.savefig("2019 Gender vs Years in Program")

#%%

#The Section Above, Which Focuses on the 2019 Cohort, is Finished!!

#%%

# The Section Focuses on the 2020 Cohort 

#Goal: This section will separate the females and the males in this cohort 
# by showing the percentages and status of each student
                             
#Creating a dataframe showing only the 2020 cohort



#This will be showing the number of students entering 
# the program during this year
P2020 = final.loc[final["P2020"] != "n_a"]
test2 = P2020[~P2020.isin(P2019)]

test2 = test2.dropna()
P2020F = test2.drop(['P2015', 'P2016', 'P2017', 'P2019', 'P2020', 'P2021'], 
                    axis=1)
print(P2020F)


#Calculating the total number of students in the program
P2020_totalstudents = len(P2020F.index)
print("\n The Total Number of Students in the 2020 Cohort")
print(P2020_totalstudents)


#Identifying the females in the 2020 cohort
female_P2020 = P2020F['Sex'].value_counts()["F"]
print("\n Cohort 2020 Females")
print(female_P2020)



#Calculating what percentage of females
female_P2020_percentage = female_P2020 / P2020_totalstudents
print("\n 2020 Female Percentage")
print(female_P2020_percentage)


#Identifying the males in the 2020 cohort
male_P2020 = P2020F['Sex'].value_counts()["M"]
print("\n 2020 Male Count")
print(male_P2020)


#Calculating what percentage of males
male_P2020_percentage = male_P2020 / P2020_totalstudents
print("\n 2020 Male Percentage")
print(male_P2020_percentage)


#Creating a Pie Chart that Shows the Aggregate of Male and Females
P2018F.groupby(['Sex']).sum().plot(
    title="2020 Cohort of Males vs Females in Program", kind='pie',
    y='Number of Years in Program', autopct='%1.0f%%')
plt.savefig("2020 Gender vs Years in Program")

#%%

#The Section Above, Which Focuses on the 2020 Cohort, is Finished!!

#%%


#Saving the script

UB_info.to_csv("project.csv")