Part III - Dictionary
Q6:
  import csv
import re

f = open("faculty.csv")
txt = f.read()[1:]
header = txt.splitlines()[:1]
lines = txt.splitlines()[1:]

csv_f = csv.reader(lines)

degree_dict = {}
degree_list = []
for row in csv_f:
    degree_list.append(row)

length = len(degree_list)
for i in range(length):
    degree_dict[degree_list[i][0]] = degree_list[i][1:]

list_keys = sorted(degree_dict)
new_dict = {}
for j in range(length):
    lastword =  list_keys[j].split()[-1]
    
    if lastword in new_dict:
        new_dict[lastword].append(degree_dict[list_keys[j]])   
    else:
        new_dict[lastword] = degree_dict[list_keys[j]]

        for i in range(3):
    print new_dict.popitem()
f.close()

Q7:
import csv

f = open("faculty.csv")
txt = f.read()[1:]
header = txt.splitlines()[:1]
lines = txt.splitlines()[1:]

csv_f = csv.reader(lines)

faculty_dict = {}
faculty_list = []
for row in csv_f:
    faculty_list.append(row)

length = len(faculty_list)
for i in range(length):
    if faculty_list[i][2].split()[0] == "Associate":
        faculty_list[i][2] = "Associate Professor"
    else:
        faculty_list[i][2] = "Professor"
    lastname = faculty_list[i][0].split()[0]
    firstname = faculty_list[i][0].split()[-1]
    new_name = (str(lastname) + " " + str(firstname))
    faculty_dict[firstname,lastname] = faculty_list[i][1:]
print faculty_dict
f.close()

Q8:
  
import csv

f = open("faculty.csv")
txt = f.read()[1:]
header = txt.splitlines()[:1]
lines = txt.splitlines()[1:]

csv_f = csv.reader(lines)

faculty_dict = {}
faculty_list = []
for row in csv_f:
    faculty_list.append(row)

length = len(faculty_list)
for i in range(length):
    if faculty_list[i][2].split()[0] == "Associate":
        faculty_list[i][2] = "Associate Professor"
    else:
        faculty_list[i][2] = "Professor"
    firstname = faculty_list[i][0].split()[0]
    lastname = faculty_list[i][0].split()[-1]
    new_name = (str(lastname) + " " + str(firstname))
    faculty_dict[lastname,firstname] = faculty_list[i][1:]


for key in sorted(faculty_dict):
    print key, faculty_dict[key]
    
f.close()
