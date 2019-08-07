import csv
from collections import defaultdict

columns=defaultdict(list)
print(type(columns))

with open('employee_birthday.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)

print(columns['Year'])
print(columns['Variable_code'])
