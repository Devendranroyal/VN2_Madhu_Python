'''
REQ:  Get/Retrieve persisted strings along with its length

CRUD           - Retrieval
Datattypes     - int string
STATE, BEHVAIOR -
'''
from _22_2_DB_String._3_RETRIEVE_strs._1_controller import get_str_data
# UI Layer
option = input("Do you want to retrieve string info ? 1. YES 2. NO : ")

if int(option) == 1:
    resp = get_str_data()  # flask, django
    print("Final response data : ")
    resp.update({'status_code': 200})
    for each in resp['response']:
        print(each[0], " **  ", each[1])
else:
    print("Please try again !! ")
