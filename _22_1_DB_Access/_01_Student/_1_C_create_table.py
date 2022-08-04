''''
@author: madhu

https://www.tutorialspoint.com/postgresql/postgresql_python.htm
https://pynative.com/python-postgresql-tutorial/

UI    --->   Python   --->  Database
      <---    Java    <---
              .Net
'''
import psycopg2  # pip install psycopg2

# Step 1 : Get connection
# Step 2 : Get cursor on db connection
# Step 3 : Prepare SQL Query
# Step 4 : Execute SQL query
# Step 5 : Commit the transaction

import psycopg2

try:
    # Step1 : Get connection
    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            database="postgres",
                            user="postgres",
                            password="vn2@123")
    print("Connection object : ", type(conn), conn)

    # Step2 : Get cursor on db connection
    cursor = conn.cursor()
    print("Cursor object : ", type(cursor), cursor)

    # Step3: Prepare SQL Query
    query = "CREATE TABLE STUDENT1(student_id INTEGER PRIMARY KEY, name VARCHAR(100), school VARCHAR(20))"

    # Step4 : Execute sql query
    cursor.execute(query)

    # Step5: Commit the transaction
    conn.commit()
    print("** Table created successfully **")
except Exception as exce:
    print("Exception occured : ", exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()


'''
import psycopg2
try:
    conn = psycopg2.connect(host = "localhost",
                            port = "5432",
                            database="postgres",
                            user = "postgres", 
                            password = "vn2")
    cursor = conn.cursor()
    emp_table_cr = 'create table command'
    cursor.execute(emp_table_cr)
    conn.commit()
except Exception exec:
    print("Exception occured : ", exec)
finally:
    cursor.close()
    conn.close()
'''



