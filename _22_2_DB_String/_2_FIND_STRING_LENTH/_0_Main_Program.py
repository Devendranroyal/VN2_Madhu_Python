'''
REQ:  Find length of the strings given by customer and save into db

CRUD           - R
Datattypes     - int string
STATE,BEHVAIOR -
'''
'''
MVC Architecture:
==================

C - Controller ----> Controller      Controller+Service
M - Model      ----> Service+DAO     DAO
V - View       -----> UI (HTML,CSS,JS...)

UI         ----->   Controller ---> Service  ---> DAO   ---> Database
           <-----              <---          <---       <---
'''

from _22_2_DB_String._2_FIND_STRING_LENTH._1_controller import get_str_len


# CREATE RETRIEVE UPDATE DELETE

# UI Layer
if __name__ == '__main__':
    str1 = input("Enter string details  : ")
    resp = get_str_len(str1)  # flask, django
    print("String length :", resp)