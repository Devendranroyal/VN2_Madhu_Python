print("--------------Program 1-------------------")
print("Program to find  first 20 the odd and even numbers from 1 to 100")
print(" ------- 1.a. List Comprehension ------ ")
odd_even = [list(range(1, 101, 2))[0:20], list(range(2, 101, 2))[0:20]]
print("The list odd and even numbers are :", odd_even)
print(" ------- 1.b. Normal For Loop -------")
odd = []
even = []
for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
    elif i % 2 == 1:
        odd.append(i)
    else:
        continue
print("The odd numbers are :", odd[0:20])
print("The even numbers are :", even[0:20])
print(" ------- 1.c. Generator mechanism ----")


def oddNumber(s):
    b = 1
    while b <= s:
        yield b * 2
        b += 1


for i in oddNumber(20):
    print(i - 1, end=" ")
print("\n")


def evenNumber(s):
    b = 1
    while b <= s:
        yield b * 2
        b += 1


for i in evenNumber(20):
    print(i, end=" ")

print("--------------Program 2-------------------")
print("Program to find out the Average, Sum, Multiplication, Highest, Lowest and Middle element of a list of integers")
li = [10, 23, 32, 45, 25, 68, 89, 110]
print("a. Maths Approach. Write Design Steps")
"""Explanation:
1.Average:
Sum of the elements is 10+23+32+45+25+68+89+110 = 402
total number of elements is 8.
So average is  402 / 8 = 50.25
2.Sum:
adding all elements is sum 10+23+32+45+25+68+89+110 = 402
3.Multiplication:
Multiplication of the elements are 10*23*32*45*25*68*89*110
4.Highest:
elements in ascending order 10, 23, 32, 45, 25, 68, 89, 110
printing last one
5.Lowest:
elements in ascending order 10, 23, 32, 45, 25, 68, 89, 110
printing first one
6.Middle:
elements in ascending order 10, 23, 32, 45, 25, 68, 89, 110
printing middle one by using mean median
"""


def Average():
    return sum(li) / len(li)


print("Average of the list =", Average())
print("Sum of the list =", sum(li))
print("Highest of the list =", max(li))
print("Lowest of the list =", min(li))
print("Mean of the list =", Average())

print("--------------Program 3-------------------")
print("Program to find the Factorial of a number using recursion")
num = int(input("enter a number: "))


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


if num < 0:
    print("Enter a correct number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", factorial(num))

print("--------------Program 4-------------------")
print(" Program to implement Binary Search ")


def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False
    while (first <= last and not found):
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


print(binary_search([1, 2, 3, 5, 8], 6))
print(binary_search([1, 2, 3, 5, 8], 5))

print("--------------Program 5-------------------")
'''5.  For a given String.Do below actions
		a. Algorithm to find length of string
		b. Get dictionary with char as key and its count as value
		c. Find vowels,consonants count in dictionary format
		d. Find special character count
		e. Replace special characters in string with X
		f. Find upper and lower case characters in dict format '''

str1 = 'Hel%lo$ Welc0m3 t9 Py77o8 Pr03#&^inG'
print("a. Algorithm to find length of string")
# print(len(str1))
list = []
for i in str1:
    list.append(i)
print("length of string str1 is: ", len(list))

print("b. Get dictionary with char as key and its count as value")
list1 = {}
for i in str1:
    if i not in list1:
        list1[i] = 1
    else:
        list1[i] += 1
print(list1)

print("--------------Program5-------------------")
'''5.  For a given String.Do below actions
		a. Algorithm to find length of string
		b. Get dictionary with char as key and its count as value
		c. Find vowels,consonants count in dictionary format
		d. Find special character count
		e. Replace special characters in string with X
		f. Find upper and lower case characters in dict format '''

str1 = 'Hel%lo$ Welc0m3 t9 Py77o8 Pr03#&^inG'
print("a. Algorithm to find length of string")
# print(len(str1))
list = []
for i in str1:
    list.append(i)
print("length of string str1 is: ", len(list))

print("b. Get dictionary with char as key and its count as value")
list1 = {}
for i in str1:
    if i not in list1:
        list1[i] = 1
    else:
        list1[i] += 1
print(list1)

print("c. Find vowels,consonants count in dictionary format")
vcount = 0
ccount = 0
for i in str1:
    vowels = 'aeiouAEIOU'
    special_char = '[@_!#$%^&*()<>?/\|}{~:]'
    if i in vowels:
        vcount = vcount + 1
    elif i not in special_char:
        if i not in vowels:
            ccount = ccount + 1
print("Vowels count: ", vcount)
print("Consonants count: ", ccount)

print("d. Find special character count")
scount = 0
for i in str1:
    if i in special_char:
        scount = scount + 1
print("Special character count:", scount)

print("e. Replace special characters in string with X")
str2 = str1.replace('[@_!#$%^&*()<>?/\|}{~:]', "X")
print(str2)

print("f. Find upper and lower case characters in dict format")
ulcount = {'up': 0, 'lc': 0}
for i in str1:
    if i.islower():
        ulcount['lc'] += 1
    elif i.isupper():
        ulcount['up'] += 1
    else:
        pass
print(ulcount)
print("c. Find vowels,consonants count in dictionary format")
vccount = {"v": 0, "c": 0}
for i in str1:
    vowels = 'aeiouAEIOU'
    special_char = '[@_!#$%^&*()<>?/\|}{~:]'
    if i in vowels:
        vccount["v"] += 1
    elif i not in special_char:
        if i not in vowels:
            vccount["c"] += 1
print("Vowel & consonants count is", vccount)

print("d. Find special character count")
scount = 0
for i in str1:
    if i in special_char:
        scount = scount + 1
print("Special character count:", scount)

print("e. Replace special characters in string with X")
str2 = str1.replace('[@_!#$%^&*()<>?/\|}{~:]', "X")
print(str2)

print("f. Find upper and lower case characters in dict format")
ulcount = {'up': 0, 'lc': 0}
for i in str1:
    if i.islower():
        ulcount['lc'] += 1
    elif i.isupper():
        ulcount['up'] += 1
    else:
        pass
print(ulcount)

print("--------------Program 6------------------")
l1 = [1, 2, 3, ]
l2 = ["ABC", "DEF", "GHI", "JKL", "MNO"]
l3 = dict(zip(l1, l2))
print("The output dictionary is : ", l3)
# get_dict = dict.fromkeys(l1, l2)
# print(get_dict)

print("The l1 as key list is : " + str(l1))
print("The l2 as value list is : " + str(l2))
res = {}
for key in l1:
    for value in l2:
        res[key] = value
        l2.remove(value)
        break
print("The Output dictionary is : " + str(res))

print("--------------Program7-------------------")
import psycopg2

conn = psycopg2.connect(host="localhost",
                        port="5432",
                        database="postgres",
                        user="postgres",
                        password="dev@143")
print("connection is done = ", conn)
cursor = conn.cursor()
print("cursor connection is created = ", cursor)
d1 = "CREATE TABLE latop1(product_ID INT,product_name VARCHAR(200),price numeric(50),color VARCHAR(200),ram VARCHAR(200))"
cursor.execute(d1)
d2 = "INSERT INTO latop1( product_ID,product_name,price,color,ram) VALUES (1,'hp',50000,'black','4GB'),(2,'dell',25000,'grey','6GB'),(3,'apple',70000,'white','8GB')"
cursor.execute(d2)
d3 = "SELECT MAX(price) FROM latop1"
d4 = "SELECT MIN(price) FROM latop1"
d5 = "SELECT MAX(ram) FROM latop1"
d6 = "SELECT MIN(ram) FROM latop1"
cursor.execute(d3)
cursor.execute(d4)
cursor.execute(d5)
cursor.execute(d6)
cursor.commit()

print("--------------Program 8------------------")
'''8. Create Employee class with eid,name,sal,exp,rating(in years).
   Take average of exp,rating and if 
	a. Avg is less than  2 : Give 10% Hike
	b. Avg is greater than or equal to 2 and less than 5, give 20% hike
	c. Avg is greater than or equal to 5 and lessthan 8, give 30% Hike'''


class Employee:
    def __init__(self, eid, name, sal, exp, rating):
        self.sal = 0
        # def __int__(self, eid, name, sal, exp, rating):
        self.eid = eid
        self.name = name
        self.sal = sal
        self.exp = exp
        self.rating = rating

    def apply_hike(self):
        average = (self.exp + self.rating) / 2
        print("average:", average)
        print("Salary before hike is:", self.sal)
        hike = 0
        if average < 8 and average >= 5:
            hike = self.sal * 30 / 100
            print(" Hike is", hike)
        elif 2 <= average < 5:
            hike = self.sal * 20 / 100
            print(" Hike is", hike)
        elif average < 2:
            hike = self.sal * 10 / 100
            print(" Hike is ", hike)
        else:
            print("Hike is 0")
        self.sal = self.sal + hike
        print(self.name, " deserves Salary with hike: ", self.sal)


mani = Employee(323, "mani", 10000, 5, 6)
mani.apply_hike()
dev = Employee(194, "dev", 15000, 2, 2)
dev.apply_hike()

print("--------------Program 9-------------------")
print("Implement a program which covers class,instance,static,methods with proper exception handing in all methods")


class Employee:
    try:
        company_name = 'VN2 Solutions pvt ltd'

        def __init__(self, ename, eid, esal):
            self.ename = ename
            self.eid = eid
            self.esal = esal

        @instancemethod
        def show(self):
            print('Employee:', self.ename, self.eid, self.esal)
            print('Company:', self.company_name)
            # print('Company name changed to', Employee.change_company("LTI"))

        @classmethod
        def change_company(cls, name):
            print('Previous company name:', cls.company_name)
            cls.company_name = name
            print('Company name changed to:', Employee.company_name)

        @staticmethod
        def find_Employee(Employee_name):
            return ['Devendran', 'Manikanta', 'kumar']

    except Exception as e:
        print("Please enter valid input :: ")


dev = Employee('Devendran', 323, 40000)
mani = Employee('Manikanta', 12, 90000)
kumar = Employee('Kumar', 34, 70000)
dev.show()
mani.show()
kumar.show()
Employee.change_company('LTI')

print("--------------Program 10-------------------")
''' Load given text file, 
       a. Convert it to json and save into Desktop'''
# C:\Users\Lenovo\Desktop\data.txt
import json
import psycopg2

filename = 'C:\\Users\\Lenovo\\Desktop\\data.txt'
dict1 = {}
fields = ['Email', 'Identifier', 'Firstname', 'Lastname']
with open(filename) as fh:
    l = 1
    for line in fh:
        description = list(line.strip().split(",", 4))
        print(description)
        sno = 'emp' + str(l)
        i = 0
        dict2 = {}
        while i < len(fields):
            dict2[fields[i]] = description[i]
            i = i + 1
        dict1[sno] = dict2
        l = l + 1
        # print(dict2)
out_file = open("C:\\Users\\Lenovo\\Desktop\\test2.json", "w")
json.dump(dict1, out_file, indent=4)
out_file.close()
'''
b. Save all the data into database 
Use OOPs concepts in all controller,service,dao layers and use proper exception,file handling ops'''


# controller layer:Receive the data from json file,convert it to dict object,send the dict to service layer
class Controller:
    def __init__(self, file_path):
        self.f_path = file_path

    def json_to_dictionary(self):
        with open(self.f_path, "r") as json_file:
            json_content = json.load(json_file)
            return json_content

        # result = save_data(data)
        data = " "
        return json.dumps(data)


# service layer: receive the dictionary from controller layer, separate the data and send it to dao layer
class Service:
    def __init__(self, received_info):
        self.received_info = received_info

    def cleaning_data(self):
        cleaned_data = []
        for each in self.received_info:
            cleaned_data.append(list(dict1.values()))
        return cleaned_data


# dao layer receive the data from service layer,create a connection with database, prepare sql query for multiple entries,execute the sql query
# return the message
class Dao:
    def __init__(self, data_from_service, host, database, user, password, port):
        self.data_from_service = data_from_service
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    def establish_db_connection(self):
        conn = ""
        cursor = ""
        try:
            conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            cursor = conn.cursor()
        except Exception as es:
            print("Exception please Check", es)
        return [cursor, conn]

    def closing_connection(self):
        cursor, conn = self.establish_db_connection()
        cursor.close()
        conn.close()

    def data_insertion(self):
        cursor, conn = self.establish_db_connection()
        records = self.data_from_service
        query = "INSERT INTO employee_information values(%s, %s, %s, %s)"
        count = 0
        for record in records:
            cursor.execute(query, record)
            count += 1
            print("query executed")
        print("Query executed", count)
        conn.commit()
        print("Table entries inserted")
        self.closing_connection()


testing = Controller("C:\\Users\\Lenovo\\Desktop\\test2.json")
service_test = Service(testing.json_to_dictionary())
dao_test = Dao(service_test.cleaning_data(), "172.25.122.144", "postgres", "postgres", "dev@143", 5432)
dao_test.data_insertion()
print("Values successfully inserted")
