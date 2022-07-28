# PROGRAM TO READ AND WRITE  DATA FROM A FILE

out_data = open("C:/Users/madhu/Desktop/names.txt", "w")
out_data.write("Welcome to the world of Python")
print("---After writing to file DATA : ", out_data)
out_data.close()

obj = open("C:/Users/madhu/Desktop/names.txt", "r")
in_data = obj.read()
print("---Reading from file--------  : ", in_data)
obj.close()
