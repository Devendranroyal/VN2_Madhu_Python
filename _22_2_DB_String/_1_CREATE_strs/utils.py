
# utils.py utilities.py properties.py constants.py

import psycopg2
conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="vn2@123",
                        host="localhost",
                        port="5432")
