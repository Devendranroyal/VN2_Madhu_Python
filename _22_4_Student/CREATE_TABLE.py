import psycopg2


def create_tables():
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="vn2",
                            host="localhost",
                            port="5432")
    #print("type :", type(conn), conn)
    cursor = conn.cursor()
    query = "CREATE TABLE Student (eCode VARCHAR(255) PRIMARY KEY,userId VARCHAR(255),tech VARCHAR(255)," \
            "" \
            "" \
            "role VARCHAR(255),region VARCHAR(255),mobile VARCHAR(13),email VARCHAR(255))"
    cursor.execute(query)
    conn.commit()

    print("---------Table Student created successfully----------")


if __name__ == '__main__':
    create_tables()

# 1. Convert json format to python format
# 2. Server side validations [{},{},{}]
# 3. Database connection
# 4. Prepare the respective sql query
# 5. Commit the transaction and send appropriate resposne to UI
