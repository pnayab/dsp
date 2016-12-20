Q1:
import csv

f = open("faculty.csv")
txt = f.read()[1:]
header = txt.splitlines()[:1]
lines = txt.splitlines()[1:]

csv_f = csv.reader(lines)

degree_list = []
for row in csv_f:
    degree_list.append(row[1])

degree_dict = {x:degree_list.count(x) for x in degree_list}
print "There are %s different degrees" % len(degree_dict)
print "These are the frequencies %s" % degree_dict
f.close()


Q2:
import csv

f = open("faculty.csv")
txt = f.read()[1:]
header = txt.splitlines()[:1]
lines = txt.splitlines()[1:]

csv_f = csv.reader(lines)

degree_list = []
for row in csv_f:
    degree_list.append(row[2])

degree_dict = {x:degree_list.count(x) for x in degree_list}
print "There are %s different titles" % len(degree_dict)
print "These are the frequencies %s" % degree_dict
f.close()

Q3:
import csv

f = open("faculty.csv")
txt = f.read()[1:]
header = txt.splitlines()[:1]
lines = txt.splitlines()[1:]

csv_f = csv.reader(lines)

degree_list = []
for row in csv_f:
    degree_list.append(row[3])

print degree_list
f.close()

Q4:
import csv
import re

f = open("faculty.csv")
txt = f.read()[1:]
header = txt.splitlines()[:1]
lines = txt.splitlines()[1:]

csv_f = csv.reader(lines)

degree_list = []
for row in csv_f:
    degree_list.append(row[3])

domain = set()
i=0
for i in range(len(degree_list)):    
    domain.add(re.search('@.+', degree_list[i]).group())

print "There are %s different email domains" % len(domain)
print "Here is the list of unique email domains %s" % domain


f.close()
