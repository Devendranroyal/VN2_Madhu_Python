'''
@author: madhu
'''
import psycopg2
try:
    # Step1 : Get connection
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="vn2@123",
                            host="localhost",
                            port="5432")
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()
    #Step3 : Prepare sql query
    query = "SELECT * FROM STUDENT1"
    #Step4 : Execute sql query
    cursor.execute(query)
    # print("Selection : ",cursor.fetchall())
    #Step4 : Retrieve Records
    print("\n-----Retrieving records from db table Test-------")
    records = cursor.fetchall()
    print("Records from db ", records)
    for each in records:
        print(each)
except Exception as exce:
    print("Exception occured : ", exce)
finally:
    print("\nClosing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()