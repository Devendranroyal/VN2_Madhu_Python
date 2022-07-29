# VN2_Madhu_Python

Introduction to Python
1.1 Introduction to Python
1.2 Beginning with Python programming
1.3 Features of Python
1.4 Dynamically Typed
1.5 Advantages  
1.6 Disadvantages 
1.7 Applications 


1.1 Introduction To PYTHON

Python is a high-level, general-purpose and a very popular programming language. 
Python programming language (latest Python 3) is being used in web development, Machine Learning applications.

Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code.
Python is a programming language that lets you work quickly and integrate systems more efficiently.
There are two major Python versions: Python 2.X(2.7) and Python 3.X Both are quite different.

1.2 Beginning with Python programming:

1) Finding an Interpreter:
Before we start Python programming, we need to have an interpreter to interpret and run our programs. There are certain online interpreters like 
https://ide.geeksforgeeks.org/ that can be used to run Python programs without installing an interpreter.
Windows: There are many interpreters available freely to run Python scripts like IDLE (Integrated Development Environment) that comes bundled with the Python software downloaded from http://python.org/. Local DEV TEST UAT PROD 
Linux: Python comes preinstalled with popular Linux distros such as Ubuntu and Fedora. To check which version of Python you’re running, type “python” in the terminal emulator. The interpreter should start and print the version number.
macOS: Generally, Python 2.7 comes bundled with macOS. You’ll have to manually install Python 3 from http://python.org/.

2) Writing our first program:
Just type in the following code after you start the interpreter.
# Script Begins 
print("welcome to python")
  
# Scripts Ends
Output:
welcome to python
Let’s analyze the script line by line.
Line 1: [# Script Begins] In Python, comments begin with a #. This statement is ignored by the interpreter and serves as documentation for our code.
Line 2: [print(“welcome to python”)] To print something on the console, print() function is used. This function also adds a newline after our message is 
printed(unlike in C). Note that in Python 2, “print” is not a function but a keyword and therefore can be used without parentheses. However, in Python 3, it is a function and must be invoked with parentheses.
Line 3: [# Script Ends] This is just another comment like in Line 1.
Python designed by Guido van Rossum at CWI has become a widely used general-purpose, high-level programming language.

Reason for increasing popularity
1.Code readability, shorter codes, ease of writing
2.Programmers can express logical concepts in fewer lines of code in comparison to languages such as C++ or Java.
3.Python supports multiple programming paradigms, like object-oriented, imperative and functional programming or procedural.
4.There exists inbuilt functions for almost all of the frequently used concepts.

1.3.Features Of Python :

i. Interpreted
○ There are no separate compilation and execution steps like C and C++.
○ Directly run the program from the source code.
○ Internally, Python converts the source code into an intermediate form called bytecodes which is then translated into native language of specific computer to run it.
○ No need to worry about linking and loading with libraries, etc.

ii. Platform Independent
○ Python programs can be developed and executed on multiple operating system platforms.
○ Python can be used on Linux, Windows, Macintosh, Solaris and many more.

iii. Free and Open Source; Redistributable

iv. High-level Language
○ In Python, no need to take care about low-level details such as managing the memory used by the program.

v. Simple
○ Closer to English language; Easy to Learn
○ More emphasis on the solution to the problem rather than the syntax
        
vi. Embeddable
○ Python can be used within C/C++ program to give scripting capabilities for the program’s users

vii. Robust:
○ Exceptional handling features
○ Memory management techniques in built

viii. Rich Library Support
○ The Python Standard Library is very vast.
○ It can help do various things involving regular expressions, documentation generation, unit testing, threading, databases, web browsers, CGI, email, XML, HTML, WAV files, cryptography, GUI and many more.
○ Besides the standard library, there are various other high-quality libraries such as the Python Imaging Library which is an amazingly simple image manipulation library.


Python vs JAVA
![image](https://user-images.githubusercontent.com/54701895/181763186-1c26ad14-6ee0-4873-b808-2e03a8569788.png)

1.4 Dynamically Typed: 

int x = 10     # Int  type    x  variable  =  Operator 10  value
In Python , No need to declare the data type. whereas in java or c we have to declare the data type.
Statically typed languages perform type checking at compile-time, while dynamically-typed languages perform type checking at run-time. 
Statically-typed languages require you to declare the data types of your variables before you use them, while dynamically-typed languages do not.


In Python:
x = 10
print(“Hello”)

Whereas in java, we need to declare data type
Java Code
public class HelloWorld
{
   public static void main (String[] args)
   {
      System.out.println("Hello, world!");
   }
}
Python Code
print("Hello, world!")
Similarity with Java
● Require some form of runtime on your system (JVM/Python runtime)
● Can probably be compiled to executables without the runtime (this is situational, none of them are designed to work this way)



GUI
![image](https://user-images.githubusercontent.com/54701895/181763649-1711967c-0325-4af7-8d03-acfa39f15b60.png)

Command Line interface
![image](https://user-images.githubusercontent.com/54701895/181763703-271f720b-377c-4844-b165-01b1d2651008.png)


1.5.Advantages : 

1.Presence of third-party modules 
2.Extensive support libraries(NumPy for numerical calculations, Pandas for data analytics etc) 
3.Open source and community development 
4.Versatile, Easy to read, learn and write
5.User-friendly data structures 
6.High-level language 
7.Dynamically typed language (No need to mention data type based on the value assigned, it takes data type) 
8.Object-oriented language 
9.Portable and Interactive
10.Ideal for prototypes – provide more functionality with less coding
11.Highly Efficient(Python’s clean object-oriented design provides enhanced process control, and the language is equipped with excellent text processing and integration capabilities, as well as its own unit testing framework, which makes it more efficient.)
12.(IoT)Internet of Things Opportunities
13.Interpreted Language
14.Portable across Operating systems 
15.Ease of use
16.Multi-paradigm Approach

1.6.Disadvantages :

1.Slow speed of execution compared to C,C++
2.Absence from mobile computing and browsers
3.For the C,C++ programmers switching to python can be irritating as the language requires proper indentation of code. Certain variable names commonly used like sum are functions in python. So C, C++ programmers have to look out for these.
4.Slow speed of execution compared to C,C++
5.Absence from mobile computing and browsers
6.For the C,C++ programmers switching to python can be irritating as the language requires proper indentation of code. Certain variable names commonly used like sum are functions in python. So C, C++ programmers have to look out for these.

1.7 Applications : 
![image](https://user-images.githubusercontent.com/54701895/181763792-edb9c668-7b56-40ac-81fe-acc92949bc57.png)

1.GUI based desktop applications
2.Graphic design, image processing applications, Games, and Scientific/ computational Applications
3.Web frameworks and applications 
4. Enterprise and Business applications 
5. Operating Systems 
6.Education
7.Database Access
8.Language Development 
9. Prototyping 
10.Software Development
11. Organizations using Python : 
      1.Google(Components of Google spider and Search Engine) 
      2.Yahoo(Maps) 
      3.YouTube 
      4.Mozilla 
      5.Dropbox 
      6.Microsoft 
      7.Cisco 
      8.Spotify 
      9.Quora 



VARIABLES

2.1Introduction                       Page 1
2.2Tokens and their types             Page 3

Write Operation:
-------------------------
x = 10
 Writing data        00001010   <-> 1 byte 
		00001010

0    0     0     0   1    0   1   0  

Print(x)  : Read operation
x = 10    : Write operation
=================================
Step1 :  First python starts executing RHS
Step2 :  It will check whether value exists  or any expression
=> If value 
		-> Here value 10 will be converted to binary format 1010   
			 -----------------
		 	|0|0|0|0|1|0|1|0|
		 	----------------- 
  	=> If expression 
             		-> First it simplifies the expression, gets final value 
             		-> Then follows above procedure

 Step3: Binary format address (memory allocation address) will be given to variable LHS

print(x) : Read operation
==========================
 - Python will go to the address of x variable
 - It will take the binary value from that address and converts to decimal format
 - Returns value to console


Data types:

1.Numbers: 
integer     :    10, 123, 432   
float       :    32.43,  543.56,  3456.34
complex     :    4+5j(Will never use)
long        :    7406900500, 324324324324(Removed)

binary  2   octa 8    deca 10    hex 16

2.Boolean:
True    - 1 bit     1
False   - 1 bit     0
x     =   10          # x = int(10)
LHS = RHS
X   =   10+20+30    10.__add__(20)    # def add(self, var):

X = 10        1010
0	0	0	0	1	0	1	0
7         6           5          4       3          2           1         0
576543424

x = 10
   LHS = RHS
- We are assigning the value 10 to variable 'x'
          value = 10
          variable = x
- Program execution starts from right to left
- LHS -> should always be a variable
-  RHS -> finally should become value
(end result/final output)

- Digital 0 1 binary format (number, audio, video, image, content)

 1 byte - 8 bits     0  00000000  to 255   11111111
0	0	0	0	1	0	1	0

 1024 bytes - 1KB
 1024 KB    - 1MB
 1024 MB    - 1GB
 
| | | | | | | | |
 Variable is a name which is used to refer memory location of value. 
 Variable also known as identifier and used to hold value.
 A variable, as the name indicates is something whose value is changeable over time.  x = 10
 In Python, we don't need to specify the type of variable (int, float) because Python is a type infer language and smart enough to get variable type.
x = 10     int x = 10;
y = 11.2
10 + 15.5 =>   10.0 + 15.5  => 25.5



 Rule : Variable names can be a group of both letters and digits, but they have to begin with a letter or an underscore.
_abc   abc    x   _x123  _123 
123  Wrong
 It is recommended to use lowercase letters for variable name. Rahul and rahul both are two different variables.
Note - Variable name should not be a keyword.
 Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Therefore, by assigning different data types to variables, you can store integers, decimals or characters in these variables.

x = 10   # Python 
int x = 10;
float x = 10.5;           # Java
bool is_active = True;  
 

2L  5L                 Memory       Water   
---------------------------------------------
int x   = 10      => 2L can    2L water
float x = 10.5  =>  5L can   5L water
float x = 10   =>  5L can   2L water
int x = (int)10.5     =>  2L can   5L water 
Implicit casting(OK),  Explicit casting(XXX)

X = 10
1. Python interpreter allocates memory(2 bytes)  
2. Converts to binary format  (00010100)
3. Copy above binary data to reserved memory
4. Give address of above memory location to variable “x”

Declaring Variable and Assigning Values:
JAVA/Others :
int x;           Declaration of variable
x = 10           Initialization
=========================================
int x = 10;      Initialization
=========================================
expression vs equation
x2+y+z            --- expression
x2+y+z = 100      --- equation / statement in python
Python :
x = 10          Initialization of variable x

Python does not bound us to declare variable before using in the application. Python variables do not need explicit declaration to reserve memory space.It allows us to create variable at required time.
We don't need to declare explicitly variable in Python. When we assign any value to the variable that variable is declared automatically.
The equal (=) operator is used to assign value to a variable.
The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.
For Ex :   age = 20   x = 20
In above ex. operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable. For example 

e_count = 10  # An integer assignment
miles   = 2.5  # A floating point
emp_name = "Madhu"   # A string
print(e_count)
System.out.println(counter); # JAVA
printf(miles)
print(miles) 
print(name)
Here, 100, 1000.0 and "Madhu" are the values assigned to counter, miles, and name variables, respectively. This produces the following result −
100
1000.0
Madhu

Multiple Assignment
i`. Assigning single value to multiple variables
Python allows you to assign a single value to several variables simultaneously. For example −
a = b = c = 10
Here, an integer object is created with the value 1, and all three variables are assigned to the same memory location. 
ii.Assigning multiple values to multiple variables:
You can also assign multiple objects to multiple variables. For example −
a, b, c = 1, 2.5, True
Here, two integer objects with values 1 and 2 are assigned to variables a and b respectively, and one string object with the value "john" is assigned to the variable c.
The values will be assigned in the order in which variables appears.

2.2 Tokens and their types :

o   Tokens can be defined as a punctuator mark, reserved words and each individual word in a statement.
o   Token is the smallest unit inside the given program.
There are following tokens in Python:
identifiers     operator              literals          Keywords    constant    
--------------------------------------------Identifiers     Operator     Literals   
x                      =                10
Keywords      
a.Keywords :
Are reserved words and has specific meaning in a language and they cannot be used as ordinary identifiers.

b.Identifiers :
An identifier is a variable name. A Python identifier is a name used to identify a variable, 
function name, 
class name, 
module name or   
other object name.
An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9)
Rules for writing Identifiers:
There are some rules for writing Identifiers. 
But first you must know Python is case sensitive. That means Name and name are two different identifiers in Python. 
Here are some rules for writing Identifiers in python.  PEP8 standards 
https://www.python.org/dev/peps/pep-0008/
_age     emp_name  emp_sal   student_id
 Identifiers can be combination of uppercase and lowercase letters, digits or an underscore(_). So myVariable, variable_1, variable_for_print all are valid python identifiers.
 An Identifier can not start with digit. So while variable1 is valid, 1variable is not valid.
 We can’t use special symbols like !,#,@,%,$ etc in our Identifier.
 Identifier can be of any length.
msg  = ‘My name is Madhu’
Though these are hard rules for writing identifiers, also there are some naming conventions which are not mandatory but rather good practices to follow.

Naming Conventions:
1.Class names start with an uppercase letter. 
2.All other identifiers start with a lowercase letter. _age   __age__
3.Starting an identifier with a single leading underscore indicates the identifier is private.
4.If the identifier starts and ends with two underscores, than means the identifier is language-defined special name.
5.While c = 10 is valid, writing count = 10 would make more sense and it would be easier to figure out what it does even when you look at your code after a long time.
6.Multiple words can be separated using an underscore, for example this_is_a_variable.
c = 10        emp_id = 10
x = 123.45    mobile_bill = 123.45

c.Literals :
In computer science, a literal is a notation for representing a fixed value  in source code.
name = “Madhu”   --- String literal
age = 10  --- integer literal
sal = 123.45 – float literal
age = 10+20
The literals include the string, unicode string, integer, float,  list, tuple and dictionary types

d.Operators :
Operators are special symbols in Python that carry out arithmetic or logical computation.The value that the operator operates on is called the operand
>>> 2 + 3
5
		Here + is an operator which is performing arithmetic computation.
		2 and 3 are the operands and 
5 is the output of the operation.

e.Constants
A constant is a type of variable whose value cannot be changed. It is helpful to think of constants as containers that hold information which cannot be changed later.
Non technically, you can think of constant as a bag to store some books and those books cannot be replaced once placed inside the bag.

Assigning value to a constant in Python:
age = 10   # variable
PI = 3.14   22/7 # PI constant
GRAVITY  =  9.8    # GRAVITY is a constant
WEEKS = {MON,TUE,WED,THU,FRI,SAT}

