import sys
import csv
import re
data = []
mobile_data = []
with open('phone_dataset.csv', 'r') as csv_data:
    readCSV = csv.reader(csv_data, delimiter=',')
    for each in readCSV:
        data.append(each[0].split(','))
    print(data)
    for record in data:
        dataset = []
        for each in record:
            dataset.append(each.strip())
        mobile_data.append(dataset)
print(mobile_data)
with open('query.txt','r') as t:
    input_data = t.read()
in_data = input_data.split('\n')
print(in_data)
sys.stdout=open("output.txt","w")
for each in in_data:
    print('Matches for:',each)
    count = 0
    for lst in mobile_data:
        if each in lst:
            count += 1
            if bool(re.search(r'\d', lst[2])):
                lst[2],lst[3] = lst[3],lst[2]
                if lst[3].isnumeric():
                    lst[3] = re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', lst[3])
                output = print('Result',count,':',lst[0],',',lst[1],',',lst[2],',',lst[3])
            else:
                output = print('Result',count,':',lst[0],',',lst[1],',',lst[2],',',lst[3])
    else:
        if count == 0:
            print('No results found')
sys.stdout.close()
