

#my_file = open("C:/Users/madhu/Desktop/python_data.txt", 'r')

my_file = open("test.txt", 'r')
print("----------------------")
# Read data from file
for line in my_file:  # list of strings
    print(line)
    if 'python' in line.split():  # list of words of each line
        print("YES :", line)
    else:
        print("------- NO ------- ")
    print("-------------------------------")
'''        
# Read data from file
for each_line in my_file:
    words = each_line.split()
    print(words)
'''
my_file.close()
print("End of program")

