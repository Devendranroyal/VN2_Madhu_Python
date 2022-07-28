# 2. Retrieval  list       List,int var +   for loop
# https://docs.python.org/3/library/pdb.html
import pdb
l1 = [10, 20, 35, 43, 54, 56, 78, 32]
print("Given list is :", l1)
length = 0
print("Length is : ", length)
for each in l1:
    length += 1

pdb.set_trace()
list1 = [1, 2, 3]
list1.append(10)
print("hello")


# 1. Write print statements where ever required  III
# 2. Deploy the application/Run the moudule debugging mode by setting break points   I
# 3. pdb module                       II

# If we are not able to deploy the application in debug mode,either use 1 or 3 approach


# pdb commands
'''
Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    
'''