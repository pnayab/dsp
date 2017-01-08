# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
import re

f = open("football.csv")
txt = f.read()[1:]
header = txt.splitlines()[:1]
lines = txt.splitlines()[1:]

csv_f = csv.reader(lines)

goals = {}
v=[]
k=[]

for row in csv_f:
    difference = int(row[-3]) - int(row[-2])
#    goals[(row[0])] = difference
    v.append(row[0])
    k.append(abs(difference))

print "the team which has the smallest difference in 'for' and 'against' goals is ", v[k.index(min(k))]
print " the diff is goals is", (min(k))
