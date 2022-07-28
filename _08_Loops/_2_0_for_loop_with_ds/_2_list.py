x = 10
m_bill = 10
print("--------For loop with list-------")

list1 = [10, 32, 43, 13, 45, 65, 24, 75, 12]
for num in list1:
    print("Number : ", num)

emp_ids = [10, 32, 43, 13, 45, 65, 24, 75, 12]
for eid in emp_ids:  # eid e_id empid emp_id
    print("Employee id : ", eid)

print("Square of each values in list ")

list1 = [1,2,3,4,5,6,7]
for each in list1:
    print("Square : ", each*each)

for s_no in [10, 32, 43, 13, 45, 65, 24, 75, 12]:  # stu_no
    print("Student no : ", s_no)

print("---------Get only even numbers -----------")
list1 = [10, 32, 43, 13, 45, 65, 24, 75, 12]
# Iterate based on value

for val in list1:
    if val % 2 == 0:
        print(val)




print("---------Print only indexes of list  -----------")

# Print only indexes
list1 = [10, 32, 43, 13, 45, 65, 24, 75, 12]
le = len(list1)  # 9

for ind in range(le):  # 0 to 8
    print(ind)

print("----------Value based on index---------------------")
# ***** Iterate based on index
le = len(list1)
for ind in range(le):  # range(9)   0 to 8
    print(ind, "-----", list1[ind])


le = len(list1)
ind = 0
while ind < le:
    print(list1[ind])
    ind += 1



print("---------------------")

for val in list1:
    print(10)
    print(32)
    print(24)
    print(12)
