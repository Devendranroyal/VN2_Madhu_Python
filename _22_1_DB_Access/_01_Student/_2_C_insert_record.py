'''
@author: madhu
'''
import psycopg2

try:
    #Step1 : Get connection
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="vn2@123",
                            host="localhost",
                            port="5432")
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()

    records = [(101, 'MADHU', 'ABC'), (102, 'Prakash', 'AREM'), (103, 'Kiran', 'VN2')]
    query = "INSERT INTO STUDENT1 VALUES(%s, %s, %s)"
    count = 0
    for record in records:
        cursor.execute(query, record)
        count += 1
        print("Query executed")
    print("Query execution : ", count)
    #Step3 : Prepare sql query
    '''
    rec1 = "INSERT INTO STUDENT values(100, 'MADHU', 'ABC')"
    rec2 = "insert into student values(101, 'Prakash', 'AREM')"
    rec3 = "insert into STUDENT values(102, 'Kiran', 'VN2')"
    # Step4 : Execute sql query
    cursor.execute(rec1)
    cursor.execute(rec2)
    cursor.execute(rec3)
    print("Insertion : ", res)
    '''
    #Step4: Commit the transaction
    conn.commit()
    print("Records inserted successfully")
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()