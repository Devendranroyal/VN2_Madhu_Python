''''''

'''
    Part I                     Part II           Part III
    UI                        --> PL        ---> Database
    (HTML,CSS,Javascript)        (Python)        (Mysql, Postgresql, Mongodb)

UI --1-->                    Python                                   ----> Database
         --2.I-->  Controller  --2.II-->  Service  --2.III-->  DAO -->
         <--3.3--              <--3.2--             <--3.1--       <--

Layer Responsibilities:
     I. Controller --> Receive input from customer(UI), validate it.
    II. Service    --> Implement business logic
   III. DAO        --> Prepare query and interact with database,get results
'''
'''
Mobileno : Client validations --> 10 digit,all numbers  
           Server validations --> valid no or not  

'''

'''
Controller   :
---------------
     1. Receive the request data from UI,     (json,xml to dict) 
   2.1. Perform server side validations and
         if success: Pass the data to Service layer
         else      : Send error response  to UI
   2.2. Pass the data to Service layer
     3. Receive response from Service layer 
     4. Prepare resp data and send to UI
             
'''


from _22_2_DB_String._1_CREATE_strs._2_service import get_length

# Controller
def get_str_len(in_str):
    print("-- CONTROLLER Layer :: ----")
    if in_str == '':
        return "Enter valid string"
    else:
        word_data = get_length(in_str)
        print("--CONTROLLER Layer :: End response : ", word_data)
        return {'user_id': word_data[0],
                'st_len': len(word_data[1].keys()),
                'words': list(word_data[1].keys())}

