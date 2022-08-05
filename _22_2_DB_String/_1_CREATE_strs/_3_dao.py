


''''''

'''
DAO  Data Access Object: 
                1. Receive the data from service
                2. Get db connection,cursor etc.,
                3. Prepare and execute the sql query with data 
                4. Send response to Service
'''
from _22_2_DB_String._1_CREATE_strs.utils import conn
'''
hello,world,welcome,to,python,MadhuNettem
USER_DATA
-----------
user_id      statement                      word_length
MadhuNettem  hello,world,welcome,to,python  5
MadhuNettem  hello,world,welcome,to,python  5
MadhuNettem  hello,world,welcome,to,python  5

'''
def save_to_db(u_id, words, length):
    try:
        print("-- DAO Layer :: ----")
        cursor = conn.cursor()
        # Create table create table USER_DATA(user_id varchar(100), statement varchar(100) primary key, length int)
        query = "INSERT INTO USER_DATA1 VALUES(%s,%s,%s)"
        print("--DAO Layer :: Inserted data :", u_id, words, length)
        cursor.execute(query, (u_id, words, length))
        conn.commit()
        return True
    except Exception as e:
        print("Exception details : ", e)
    finally:
        cursor.close()
        conn.close()
