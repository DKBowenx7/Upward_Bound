# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:28:58 2023

@author: dkbow
"""


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

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

print("\n Total Number of Females Per Zip Code")
print(male_final)


#Combining male and female students to see the aggregated total of pupils 
#per zip code. 

zip_gender = pd.merge(male_final, female_final, on='Zip', how = 'left')
zip_gender = zip_gender.fillna(0)
print("\n Total Students Per Zip Code")
print(zip_gender)


zip_gender.plot(x="Zip", y=["The Total Number of Male Students", 
"The Total Number of Female Students"],
title= "Total Number of Upward Bound Students Per Home Zip Code", 
kind="bar", figsize=(10, 9))

plt.show()

#%%

# The Above That Focuses Primarily on Students Home Zip Codes Are Completed


#%%
                                                
# This Section's Goal is to look at Each Student's Participation Status 
# in the Program 

# It will later be illustrated by Bar Charts
# Looking at how many students dropped out of program total 
# & then male vs female



# This line of code is looking at each student's status in 
# the program for 2020.
# Reasoning: Since this was during the height of COVID-19, 
#I want to see if there is any significant changes compared to other years.


student_status = final.drop(final.columns[[0, 4, 5, 6, 7, 8, 10]],
                                            axis=1, inplace=False)


student_status.loc[student_status["P2020"] 
                   == "Moved", "P2020"] = "Discontinued"


print(final["P2020"].value_counts()["Discontinued"] + final["P2020"]
                                            .value_counts()["Moved"])


print("\n Each Student's Involvement Status with a Focus of 2020")

print(student_status)




#This group of coding is focusing on female students participation in 2020

#This code separates females from males. So, the only results will be on 
# the female pupils status

female_only = student_status[student_status.Sex != "M"]

female_only = female_only['P2020'].value_counts().reset_index().set_axis(
                ['P2020','The Number of Female Students in 2020'], axis=1)

print("\n Female Students 2020 Paticipation Status")
print (female_only)




# This group of coding is focusing on male students participation in 2020

# This code separates males from females. So, the only results will be on 
# the male pupils status

male_only = student_status[student_status.Sex != "F"]

male_only = male_only['P2020'].value_counts().reset_index().set_axis(['P2020',
                            ' The Number of Male Students in 2020'], axis=1)

print("\n Male Students 2020 Paticipation Status")
print (male_only)





#This group of coding below will be combining the 2020 status and illustrating 
#it in a bar graph

#This code is merging the female and male only status to create an aggregate

true_dropped = pd.merge(male_only, female_only, on='P2020', how = 'left')
print("\n A Merged Table of All Students' 2020 Participation Status")
print(true_dropped)


true_dropped.loc[true_dropped["P2020"] == "X", "P2020"] = "In Program"


#This Code is Creating the Bar Chart for Visualization
true_dropped.plot(x="P2020", y=[" The Number of Male Students in 2020", 
"The Number of Female Students in 2020"],
title= "Male vs Female Students in Program", kind="bar", figsize=(10, 9))

plt.xlabel('Status of Students in Program')
plt.ylabel("Total Number of Students")
plt.show()

#%%

# The Above That Focuses Primarily on Students in 2020 is Completed.


#%%

# In this Section, the focus will primarily be about cohort 1


# X symbolizes that students are actively participating in the program.
X = ['2015-2016','2016-2017','2017-2018','2018-2019', '2019-2020']
inProgram = [26, 25, 22, 21, 0]
Discontinued = [0, 1, 4, 5, 0]
inCollege = [0, 0, 0, 0, 21]
unknown = [0, 0, 0, 0, 5]

#These codes will be creating the bar graphs. 
barWidth = 0.40
fig = plt.subplots(figsize =(12, 8))
br1 = np.arange(len(X))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]


plt.bar(br1, inProgram, color ='g', width = barWidth, edgecolor ='grey', 
        label = "In Program")

plt.bar(br2, Discontinued, color ='y', width = barWidth, edgecolor ='grey', 
        label ='Discontinued')

plt.bar(br3, inCollege, color ='b', width = barWidth, edgecolor ='grey', 
        label ='In College')

plt.bar(br4, unknown, color ='y', width = barWidth, edgecolor ='grey', 
        label ='Unknown')


plt.xticks([r + barWidth for r in range(len(br1))], ['2015', '2016', '2017',
                                                     '2018', '2019'])
plt.xlabel("Years")
plt.ylabel("Number of Students")
plt.title(" Cohort 1: Overall Student Status")
plt.legend()
plt.show()




# The codes below for cohort 1 is showing a timelapse of students' 
# participation in the program


# X symbolizes that students are actively participating in the program.
X = ['2015-2016','2016-2017','2017-2018','2018-2019', '2019-2020', 
     '2020-2021', '2021-2022']

male_in_program = [11, 10, 9, 8, 0, 0, 0]

female_in_program = [15, 15, 13, 13, 0 ,0 ,0]

barWidth = 0.40

fig = plt.subplots(figsize =(12, 8))
br1 = np.arange(len(X))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br2, male_in_program, color ='b', width = barWidth, edgecolor ='grey',
        label = "Male Students")

plt.bar(br3, female_in_program, color ='g',width = barWidth, edgecolor ='grey',
        label ='Female Students')

plt.xticks([r + barWidth for r in range(len(br1))], ['2015', '2016', '2017', 
                                            '2018', '2019', '2020', '2021'])
plt.xlabel("Years")
plt.ylabel("Number of Students")
plt.title("Cohort One 4 Year View: Retention Rate of Males vs Female")
plt.legend()
plt.savefig("Cohort1_4years_of_highschool")
plt.show()


#%%

# The Above That Focuses Primarily on Cohort 1 is Completed.


#%%

# In this Section, the focus will primarily be about cohort 2



# X symbolizes that students are actively participating in the program.
X = ['2015-2016','2016-2017','2017-2018','2018-2019', '2019-2020', '2020-2021',
     '2021-2022']

male_in_program  = [0, 10, 9, 8, 8, 0, 0]
female_in_program = [0, 15, 16, 13, 12, 0, 0]
barWidth = 0.40
fig = plt.subplots(figsize =(12, 8))
br1 = np.arange(len(X))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br2, male_in_program , color ='b', width = barWidth, edgecolor ='grey',
        label = "Male Students")

plt.bar(br3, female_in_program, color ='g', width = barWidth,edgecolor ='grey',
        label ='Female Students')

plt.xticks([r + barWidth for r in range(len(br1))], ['2015', '2016', '2017', 
                                            '2018', '2019', '2020', '2021'])
plt.xlabel("Years")
plt.ylabel("Number of Students")
plt.title("Cohort Two 4 Year View: Retention Rate of Males vs Female")
plt.legend()
plt.savefig("Cohort2_througout_highschool")
plt.show()


#%%

# The Above That Focuses Primarily on Cohort 2 is Completed.


#%%

# In this Section, the focus will primarily be about cohort 3


X = ['2015-2016','2016-2017','2017-2018','2018-2019', '2019-2020', '2020-2021',
     '2021-2022']

male_inprogram = [0, 0, 6, 7, 6, 5, 0]
female_inprogram = [0, 0, 20, 19, 18, 16, 0]
barWidth = 0.40

fig = plt.subplots(figsize =(12, 8))
br1 = np.arange(len(X))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br2, male_inprogram, color ='b', width = barWidth, edgecolor ='grey', 
        label = "Male Students")
plt.bar(br3, female_inprogram, color ='g', width = barWidth, edgecolor ='grey', 
        label ='Female Students')

plt.xticks([r + barWidth for r in range(len(br1))], ['2015', '2016', '2017', 
                                            '2018', '2019', '2020', '2021'])

plt.xlabel("Years")
plt.ylabel("Number of Students")
plt.title("Cohort Three 4 Year View: Retention Rate of Males vs Female")
plt.legend()
plt.savefig("Cohort3_throughout_highschool")
plt.show()

#%%

# The Above That Focuses Primarily on Cohort 3 is Completed.

#%%

# In this Section, the focus will primarily be about cohort 4

X = ['2015-2016','2016-2017','2017-2018','2018-2019', '2019-2020', '2020-2021',
     '2021-2022']

male_inprogram = [0, 0, 0, 6, 5, 4, 4]
female_inprogram = [0, 0, 0, 10, 10, 8, 8]
barWidth = 0.40
fig = plt.subplots(figsize =(12, 8))
br1 = np.arange(len(X))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br2, male_inprogram, color ='b', width = barWidth, edgecolor ='grey',
 label = "Male Students")

plt.bar(br3, female_inprogram, color ='g', width = barWidth, edgecolor ='grey',
label ='Female Students')

plt.xticks([r + barWidth for r in range(len(br1))], ['2015', '2016', '2017',
'2018', '2019', '2020', '2021'])

plt.xlabel("Years")
plt.ylabel("Number of Students")
plt.title("Cohort Four 4 Year View: Retention Rate of Males vs Female")
plt.legend()
plt.savefig("Cohort4_throughout_highschool")
plt.show()

#%%

# The Above That Focuses Primarily on Cohort 4 is Completed.


#%%

# In this Section, the focus will primarily be about cohort 5

X = ['2015-2016','2016-2017','2017-2018','2018-2019', '2019-2020', 
     '2020-2021', '2021-2022']

inProgramMale = [0, 0, 0, 0, 5, 7, 7]
inProgramFemale = [0, 0, 0, 0, 7, 8, 8]
barWidth = 0.40
fig = plt.subplots(figsize =(12, 8))
br1 = np.arange(len(X))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br2, inProgramMale, color ='b', width = barWidth, edgecolor ='grey', 
        label = "Male Students")
plt.bar(br3, inProgramFemale, color ='g', width = barWidth, edgecolor ='grey',
        label ='Female Students')

plt.xticks([r + barWidth for r in range(len(br1))], ['2015', '2016', '2017',
                                            '2018', '2019', '2020', '2021'])
plt.xlabel("Years")
plt.ylabel("Number of Students")
plt.title("Cohort Five 4 Year View: Retention Rate of Males vs Female")
plt.legend()
plt.savefig("Cohort5_throughout_highschool")
plt.show()

#%%

# In this Section, the focus will primarily be about cohort 6

X = ['2015-2016','2016-2017','2017-2018','2018-2019', '2019-2020', '2020-2021',
     '2021-2022']

male_inprogram = [0, 0, 0, 0, 0, 7, 7]
female_inprogram = [0, 0, 0, 0, 0, 8, 8]
barWidth = 0.40
fig = plt.subplots(figsize =(12, 8))
br1 = np.arange(len(X))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br2, male_inprogram, color ='b', width = barWidth, edgecolor ='grey', 
        label = "Male Students")
plt.bar(br3, female_inprogram, color ='g', width = barWidth, edgecolor ='grey',
        label ='Female Students')

plt.xticks([r + barWidth for r in range(len(br1))], ['2015', '2016', '2017', 
                                            '2018', '2019', '2020', '2021'])
plt.xlabel("Years")
plt.ylabel("Number of Students")
plt.title("Cohort Six 4 Year View: Retention Rate of Males vs Female")
plt.legend()
plt.savefig("Cohort Six 4 Year View: Retention Rate of Males vs Female")
plt.show()

#%%

# In this Section, the focus will primarily be about cohort 7


X = ['2015-2016','2016-2017','2017-2018','2018-2019', '2019-2020', 
     '2020-2021', '2021-2022']

inProgramMale = [0, 0, 0, 0, 0, 0, 7]
inProgramFemale = [0, 0, 0, 0, 0, 0, 8]
barWidth = 0.40
fig = plt.subplots(figsize =(12, 8))
br1 = np.arange(len(X))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br2, inProgramMale, color ='b', width = barWidth, edgecolor ='grey', 
        label = "Male Students")
plt.bar(br3, inProgramFemale, color ='g', width = barWidth, edgecolor ='grey',
        label ='Female Students')

plt.xticks([r + barWidth for r in range(len(br1))], ['2015', '2016', '2017', 
                                             '2018', '2019', '2020', '2021'])
plt.xlabel("Years")
plt.ylabel("Number of Students")
plt.title("Number of Students in Cohort 7 Over Time")
plt.legend()
plt.savefig("Cohort Seven 4 Year View: Retention Rate of Males vs Female")
plt.show()

#%%

