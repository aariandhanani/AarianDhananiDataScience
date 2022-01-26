#Aarian Dhanani
#1/25/2022
#Analyzing the Diversity by Colleges CSV

import os
os.system('clear')

#1. Analyze the data set and describe some studies you could do with this data. If any bad data or values that would need to be replaced?
#We can find the percentage of minorities in each of the colleges. We can also find the percentage of women in each of the universities
#We would also need to remove the N/A data because it has one or more missing cells. We should also delete any rows with a gender in the race category. Also, we need to remove the international rows because interntional is not a race. Also remove unknown.

#2. Make a list of all the minority groups per state and add a total number of students
import csv
file = open('diversity_school.csv')
diversitySchool = csv.reader(file)
header = next(diversitySchool)
# print(header)
diversityGroups = [[0,0]]
# print(len(diversityGroups))
i = 0
worked = 0

for row in diversitySchool:
    state = row[2]
    while(i != len(diversityGroups)):
        #print(diversityGroups[i][0])
        if(state == diversityGroups[i][0]):
            diversityGroups[i][1] = int(diversityGroups[i][1]) + int(row[4])
            worked = 1
        i = i + 1
    if(worked == 0):
        # print("here")
        diversityGroups.append([row[2],row[4]])
    #print(row)
    #print(diversityGroups[i][0])
    worked = 0
    i = 0


print(diversityGroups)





#3. Make a list of the number of schools studied per state (Use dictionary key=states, value=number of schools)




#4. What is the greatest ethnic group per state?
#5. Add a column for a percentage of race per university and write to file