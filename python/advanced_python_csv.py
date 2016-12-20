import csv

f = open("faculty.csv")
txt = f.read()[1:]
header = txt.splitlines()[:1]
lines = txt.splitlines()[1:]

csv_f = csv.reader(lines)

degree_list = []
for row in csv_f:
    degree_list.append(row[3])

f.close()


with open('emails.csv', 'wb') as testfile:
    csv_writer = csv.writer(testfile, delimiter='\n')
    csv_writer.writerow([x for x in degree_list])    
