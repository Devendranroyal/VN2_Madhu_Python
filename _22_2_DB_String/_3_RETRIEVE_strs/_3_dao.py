


''''''

'''
DAO  Data Access Object: 
                1. Receive the data from service
                2. Get db connection,cursor etc.,
                3. Prepare and execute the sql query with data 
                4. Send response to Service
'''
from _22_2_DB_String._3_RETRIEVE_strs.utils import conn

def ret_strs_db():
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM  STRING_DATA"
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    except Exception as e:
        print("Exception details : ", e)
    finally:
        cursor.close()
        conn.close()
