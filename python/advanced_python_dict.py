Part III - Dictionary
Q1:
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
