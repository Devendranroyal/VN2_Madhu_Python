'''
Requirement :
1. CRUD   Create,Retrieve,Update,Delete
2. Datatype
3. State, Behavior

Numbers : int float long complex  - Immutable
Boolean : bool   - Immutable
String  : " " ' ' -  Immutable, Sequence, char based
List*    : []      -  Mutable, Sequence, Insertion order, home/hetero, duplicates allowed
Tuple   : ()      -  Immutable, Sequence, Insertion order, home/hetero, duplicates allowed
Dict*    : {}      -  Mutable, key-value pair, keys Immutable&Unique
Set     : {}      -  Mutable, inside element Immutable& Unique , no order follows

Requirement :
1. Categorize req, input data parts
2. C R U D
3. Datatype
4. State, Behavior

Requirement : Find student grade based on given marks for each student

Step 1:  Input data   : Given marks for each student
         Req(Question): Find Student grade
Step 2:  RETRIEVAL    : We are getting student grade and displaying in console
Step 3:  Datatype     : if only student marks were given : [100,20,45,67,89,43,23]
                        If rollno, marks were given      :[[12345,100],[132111,20],[3243232,45]....]
                                                         :{12345:100,
                                                           132111:20,
                                                           3243232:45
                                                           }
                                                           {12345:[100,20,45,67,89,43,23],
                                                           132111:[100,20,45,67,89,43,23],
                                                           3243232:[100,20,45,67,89,43,23]
                                                           }


                        If complete info given            :{12345:['MadhuN','10th',90,'ATP'],
                                                            132111:['KiranG','10th',85,'ATP'],
                                                            ........
                                                            }
                        Grade: String 'A' - 75 to 100,
                                      'B' - 60 to 75,
                                      'C' - 50 to 60,
                                      'D' - 35 to 50
                                     'Fail'- <35

Step 4:  State :
         Behavior:
'''
# State  --> Variables
student_info = {12345: ['MadhuN', '10th', 90, 'ATP'],
                43232: ['KiranG', '10th', 85, 'CHR'],
                42422: ['Prakash', '10th', 34, 'KRN']
                }
print("-----------------------")
# Behavior --> Functions
for sid, sinfo in student_info.items():
    marks = sinfo[2]
    if marks >= 70 and marks <= 100:
        print(sid, " grade is : ", " A")
    elif marks >= 60 and marks < 70:
        print(sid, " grade is : ", " B")
    elif marks >= 50 and marks < 60:
        print(sid, " grade is : ", " C")
    elif marks >= 35 and marks < 50:
        print(sid, " grade is : ", " D")
    else:
        print(sid, " grade is : ", " Fail")

'''
Requirement :  Find length of String
1. Categorize req,input data parts
2. C R U D  
3. Datatype   
4. State, Behavior

Requirement : Find length of given string

Step 1:  Input data   : given string
         Req(Question): Find length
Step 2:  Retrieval    : We are getting length of string 
Step 3:  Datatype     : String : 'Hello World'
Step 4:  State :
         Behavior:
'''
print("-----------------------")
# State  --> Variables
msg = 'Hello World'
# Behavior --> Functions
length = 0
for each in msg:
    length += 1
print("Length of string : ", length)


# Different ways to write program
# 1. Builtin function
l1 = [1,2,3,4]
print("Lenght of list : ",len(l1))

# 2. Normal business logic using while,if,else,for
l1 = [1,2,3,4]
le = 0
for each in l1:
    le += 1
print("Length of list : ",le)

# 3. Using functions
l1 = [1,2,3,4]
def find_length(in_list):
    le = 0
    for each in l1:
        le += 1
    return le
print("Length of list : ",find_length(l1))


# 4. Using OOPs

class FindLength:
    l1 = [1, 2, 3, 4]

    def find_length(cls):
        le = 0
        for each in cls.l1:
            le += 1
        return le

print("Length of list : ", FindLength.find_length())


# 5. Take 2nd,3rd or 4th step and include exception handling
l1 = [1,2,3,4]
def find_length(in_list):
    try:
        le = 0
        for each in l1:
            le += 1
        return le
    except:
        pass
print("Length of list : ",find_length(l1))