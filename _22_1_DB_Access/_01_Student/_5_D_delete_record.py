'''
@author: madhu

UI --> Python --> Database

'''
import psycopg2
try:
    conn = psycopg2.connect(database="postgres", 
                            user="postgres",
                            password="vn2@123",
                            host="localhost",
                            port="5432")
    cursor = conn.cursor()
    stud_id = int(input("Enter student id : "))
    cursor.execute("DELETE FROM STUDENT1 WHERE student_id = {0}".format(stud_id))
    print("Deleted record successfully")
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()