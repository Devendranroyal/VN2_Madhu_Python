''''''
'''
Service   :
---------------
             1. Receive the validated data from Controller
             2. If required interact with database for more data (dao layer call)
             3. Implement business logic as per give requirement
             4. Call dao layer(Pass the data) for data persistence
             5. Get response from DAO and send it to controller

'''
from _22_2_DB_String._3_RETRIEVE_strs._3_dao import ret_strs_db
# Business logic
def get_str_details():
    s_data = ret_strs_db()
    # print(s_data)
    resp_data = {}
    resp_data['response'] = s_data
    return resp_data