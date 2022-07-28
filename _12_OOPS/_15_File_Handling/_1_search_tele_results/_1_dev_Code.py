
'''
3 files   phone_dataset.csv  : Input data telephone directory data
          query.txt          : Customer provided names to search in tele dir
          output.txt         : Search results 

Constraints:
------------
1. First 2 positions, firstname,lastname
2. 3,4th postions: location, mobileno (if not perform swapping)
3. 9179581191 ==> (917) 958-1191
4. Search names can be either lowercase or uppercase
5. User can either give firstname or lastname.
   But we have to display results for all

SDLC Phases:
------------
Requirement Gathering
Analysis:     - Functional analysis
              - Technical analysis
Design 
Development
Testing
Deployment

Doe, John, New York, (917) 958-1191
Doe, John, California, (212) 234-1191 
John, Smith, 9179581191, New York 
Bill, Gates, (917) 358-1291, New York 
Doe, John, Florida, (919) 234-1192 

'''

import csv
import re

# To update number in US number format if given as plain number
def _update_num(mob_num):
    upd_num = '(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', mob_num))
    return upd_num

# Retrieve each user record and swap if mobile number is in 3rd position
def _get_user_data(user_data):
    print("User data : ", user_data)
    is_num = any(char.isdigit() for char in user_data[2]) # any all in python
    if is_num:
        if user_data[2].isnumeric():
            num_formt = _update_num(user_data[2])
            # num_formt = '(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', user_data[2]))
            user_data[2] = num_formt
        user_data[2], user_data[3] = user_data[3], user_data[2] 
    return user_data

# Write data to output.txt file
def _write_data_to_file(fname, phone_data,out_file):
    heading = "Matches for: "+fname
    out_file.write(heading)
    row_no = 1
    for data in phone_data.values():
        if fname in (data[0], data[1]):
            res_rec = "Result "+str(row_no)+" : "+data[0]+", "+data[1]+", "+data[2]+", "+data[3]
            out_file.write('\n')
            out_file.write(res_rec)
            row_no += 1
    if row_no == 1:
        out_file.write('\n')
        out_file.write('No results found')
    out_file.write('\n')

# Read data from csv file
def read_data_from_csv():  
    phone_data = {}
    with open('phone_dataset.csv') as file_obj:
        reader = csv.reader(file_obj)
        print("CSV Data ", reader)
        counter = 1
        for row in reader:
            print(row)
            phone_data[counter] = _get_user_data(row[0].split(','))
            counter += 1
        print("Phone data : ", phone_data)
    return phone_data

# Read query names from text and write end result  to out text file
def write_data_to_txt(p_data):
    with open('query.txt') as in_data:
        names = in_data.readlines()
        #content = [x.rstrip() for x in names]
        content = []
        for x in names:
            content.append(x.rstrip())

        print("---Search names : ", content)
        out_file = open("output.txt", "w")
        for first_name in content:
            _write_data_to_file(first_name, p_data, out_file)


if __name__ == '__main__':
    # 1. Read data from csv and store in a dictionary
    ph_data = read_data_from_csv()
    print("Phone data : ", ph_data)

    # 2. Read query users, search and retrieve results
    write_data_to_txt(ph_data)
    print("Success")