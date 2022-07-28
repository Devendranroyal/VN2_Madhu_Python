print("----------------1. Without exception handling---------------")

'''
Load 
Write/Read
Close
'''
file_obj = open("write_da1.txt", 'dew')   # C:/Users/madhu/Desktop/write_data.txt
print("File type ", file_obj, type(file_obj))
data = input("Enter text : ")
file_obj.write(data)  # TextIOWrapper.write(file_obj, data)  emp.getdata(10) ==> Employee.getdata(emp,10)
file_obj.close()
print("---Completed---")

'''
file_obj  : TextIOWrapper class 
---------
name='write_data1.txt' 
mode='w' 
encoding='cp1252'
'''


print("----------------2. With exception handling---------------")
'''
TextIOWrapper
    name='C:/Users/madhu/Desktop/write_data.txt' 
    mode='w' 
    encoding='cp1252'
'''
'''
1. Create the file # C:/Users/madhu/Destop/
2. Perform operations on file: read/write/append
3. Close the file
'''
try:
    # 1. Open the file # C:/Users/madhu/Destop/write_data2.txt
    file_obj = open("write_data2.txt", 'w')
    print("File content ", file_obj)
    print("File type :", type(file_obj))
    data = input("Enter text : ")
    # 2 Perform ops on file
    file_obj.write(data)  # ==> TextIOWrapper.write(file_obj, data)
except FileNotFoundError as fnf:
    print("File not found at specified path", fnf)
finally:
    # condition to check whether object my_file exists or not
    # 3 Close the file
    file_obj.close()
    
print("---Completed---")


print("----------------3. Using  functions---------------")
def write_data(file, f_mode):
    try:
        file_obj = open(file, f_mode)
        data = input("Enter text : ")
        file_obj.write(data)
    except FileNotFoundError as fnf:
        print("File not found : ", fnf)
    finally:
        file_obj.close()
    print("---Further business logic---")

# file_path = "C:/Users/madhu/Desktop/write_data3.txt"
file_path = 'write_data3.txt'
mode = 'w'
write_data(file_path, mode)


print("----------------4. Using OOPs concepts instance method---------------")
class FileHandling:
    def __init__(self, file_obj, mode):
        self.file_obj = file_obj
        self.mode = mode

    def write_data(self, in_data):
        try:
            file_obj = open(self.file_obj, self.mode)
            print("File type ", file_obj, type(file_obj))
            file_obj.write(in_data)  # TextIOWrapper.write(my_file,in_data)
        except FileNotFoundError as fnf:
            print("File not found at specified path")
            print(fnf)
        finally:
            # condition to check whether object my_file exists or not
            file_obj.close()

myfile = FileHandling("write_data4.txt", 'w') # C:/Users/madhu/Desktop/write_data4.txt
data = 'Hello world. This is my fourth file using oops concepts'
myfile.write_data(data)

'''
data = 'Hello world. This is my third file'
file_obj = FileHandling("C:/Users/madhu/Desktop/write_data3.txt",data)
file_obj.write_data()

file_obj = FileHandling()
file_obj.write_data(f_path,data)
'''

print("----------------5. Using OOPs concepts static method---------------")
class FileHandling:

    @staticmethod
    def write_data(file_path, in_data):
        try:
            file_obj = open(file_path, 'w+')  #1
            file_obj.write(in_data)            #2
        except FileNotFoundError as fnf:
            print("File not found at specified path", fnf)
        finally:
            file_obj.close()                   # 3

file_p = "write_data5.txt"
data = 'Fifth file using static method in oops'
FileHandling.write_data(file_p, data)