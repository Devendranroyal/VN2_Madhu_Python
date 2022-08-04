'''
@author: madhu
'''
import psycopg2
try:
    conn = psycopg2.connect(database="postgres", 
                            user="postgres",
                            password="vn2@123",
                            host="localhost",
                            port="5432")
    cursor = conn.cursor()
    query = "UPDATE STUDENT1 set name = 'MadhuSudhan Naidu Nettem' where student_id = 101"
    res = cursor.execute(query)
    print("Record Updated successfully : ", res)
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()