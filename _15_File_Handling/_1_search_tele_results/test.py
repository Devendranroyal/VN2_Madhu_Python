import csv

filename = "phone_dataset.csv"
fields = []
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(rows)
for record in rows:
    if record[2].isalpha():
