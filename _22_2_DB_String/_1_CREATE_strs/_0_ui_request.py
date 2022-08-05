'''
REQ:  Find number of words(, separated)  in a string and store the results to db

Criteria: User will give string along with his userid.
          Last word in the string can be considered as userid

hello,world,welcome,to,python,MadhuNettem

output: 5, MadhuNettem
CRUD            - Create, Retrieve
Data types      - string int
STATE, BEHAVIOR -
'''
from _1_controller import get_str_len
# UI Layer
if __name__ == '__main__':
    str1 = 'hello,world,welcome,four,python,MadhuNettem'  # input("Enter string : ")
    print("-- UI Layer :: Calling controller layer")
    str1 = 'hello,world,python,language,Nettem'
    resp = get_str_len(str1)  # calling controller layer  (flask, django)
    print("--UI Layer :: Final RESPONSE :", resp)
    print("--UI Layer :: Welcome Mr : ", resp['user_id'])
    print("--UI Layer :: Total words : ", resp['st_len'])
    print("--UI Layer :: Word details  : ")
    for word in resp['words']:
        print(word, "----", len(word))