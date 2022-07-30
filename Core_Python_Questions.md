# VN2_Madhu_Python
Core Python:
---------------------------------------------------------------------------------------------------------------------------------

PYTHON INTRODUCTION
----------------------------------------------------------------------------------------

1. PYTHON FEATURES

   --1.easy to learn
     2.easy to read
     3.easy to maintaince
     4.abroad standard library
     5.interactive mode
     6.portable
     7.python is intrepreted
     8.python is object oriented
-------------------------------------------------------------------------------------------
2. ADVANTAGES AND DISADVANTAGES
  
   -- Advantages of python

     1.It is easy to learn and use,and it has an extensive library.	   
     2.Python increases productivity.	          
     3.It is very flexible.	                          
     4.It has a very supportive community.
	        
   -- Disadvantages of python

     1.Because of its elementary programming, users face difficulty while working with other programming languages.
     2.Python is a time-consuming language. It has a low execution speed.	                        
     3.There are many issues with the design of  the language, which only gets displayed during runtime.	        
     4.It is not suited for memory-intensive programs and mobile applications.
---------------------------------------------------------------------------------------------------------------------
3. COMPILE TINE VS RUN TIME

     --- compile time is the period when the programming code is converted to machine code.
    ---  Runtime is the when a program is running and generally occurs after compile time 
 ------------------------------------------------------------------------------------------------------------------
4. WHY PYTHON IS CALLED INTREPRETTED PROGARMMING LANGUAGE

   -- python is called intrepretted langauge because it goes through an intrepreter ,which turns the code you
      write into the language understood by computers proccessor
---------------------------------------------------------------------------------------------------------------------
5. TOKENS IN PYTHON

  -- A token is the smallest individual unit in python program.all statements and instructions in a
     program are built with tokens
---------------------------------------------------------------------------------------------------------------------
6.MEMORY MANAGEMENT IN PYTHON

   -- Memory management in Python involves a private heap containing all Python objects and data structures. 
      The management of this private heap is ensured internally by the Python memory manager.
------------------------------------------------------------------------------------------------------------------
7.GARBAGE COLLECTION HOW IT WORKS

  --- python deletes unwanted objects automatically to free the memory space.the process by which periodically
      frees and reclaims the blocks of memory that no longer are in use is called garbage collection
----------------------------------------------------------------------------------------------------
8. .PY VS .PYC FILE

   -- .py files contain the source code of a program.where as .pyc file contains the byte code of your program.
--------------------------------------------------------------------------------------------------------------------------------
9.HOW PYTHON PROGRAM EXECUTES INTERNALLY

  --Step 1:  The python compiler reads a python source code or instruction. Then it verifies that the instruction is well-formatted,
             i.e. it checks the syntax of each line. If it encounters an error, it immediately halts the translation and 
             shows an error message.

  --Step 2: If there is no error, i.e. if the python instruction or source code is well-formatted then the
           compiler translates it into its equivalent form in an intermediate language called “Byte code”.

  --Step 3: Byte code is then sent to the Python Virtual Machine(PVM) which is the python interpreter.
            PVM converts the python byte code into machine-executable code.
            If an error occurs during this interpretation then the conversion is halted with an error message
--------------------------------------------------------------------------------------------------------------------------
10.PYTHON IS DYNAMICALLY PROGRAMMING LANGUAGE.WHY?

  -- We don't have to declare the type of variable while assigning a value to a variable in Python.
    Other languages like C, C++, Java, etc.., there is a strict declaration of variables before assigning values to them.
    It states the kind of variable in the runtime of the program. So, Python is a dynamically typed language

=================================================================================================================

                                2.VARIABLES
========================================================================================================
1.VARIABLE SCOPES OF LEGB RULE

   -- The LEGB rule names the possible scopes of a variable in Python: Local, Enclosing, Global, Built-in.
      Python searches namespaces in this order to determine the value of an object given its name. 
      Scopes are created with functions, classes, and modules.
-----------------------------------------------------------------------------------------------------------------------
2.MEMORY ALLOCATION OF VARIABLES

   --- memory allocation can be defined as allocating a block of space in the computermemory to a program.
       in python memory allocation and deallocation method is automatic as the python developers created a garbage
       collection for python so that the user does not have to do manual garbage collection
-------------------------------------------------------------------------------------------------------------------------
3.SWAP 2 VARIABLES WITHOUT USING THIRD VARIABLE

  
    x = 5
    y = 7
  
    print ("Before swapping: ")
    print("Value of x : ", x, " and y : ", y)
    x, y = y, x
    print ("After swapping: ")
    print("Value of x : ", x, " and y : ", y)

   Output:
    ===============
   Before swapping: 
   Value of x :  5  and y :  7
   After swapping: 
   Value of x :  7  and y :  5 
-----------------------------------------------------------------------------------------------------------------------
4.LOCAL VS GLOBAL VARIABLES .EXPLAIN IN DETAIL?

     -- Variables are classified into Global variables and Local variables based on their scope. 
        The main difference between Global and local variables is that global variables can be accessed globally in the entire program,
        whereas local variables can be accessed only within the function or block in which they are defined.

-------------------------------------------------------------------------------------------------------------------------------
                 3.OPERATORS
==========================================
1.KEY WORDS AVAILABLE IN PYTHON
   
  Keywor          Description
=============   ==================
  and	--->   A logical operator
  as	--->  To create an alias
 assert	--->  For debugging
 break	--->  To break out of a loop
 class	--->  To define a class
 continue ---> To continue to the next iteration of a loop
  def	 ---> To define a function
  del	---> To delete an object
 elif	---> Used in conditional statements, same as else if
 else	---> Used in conditional statements
 except	---> Used with exceptions, what to do when an exception occurs
False	---> Boolean value, result of comparison operations
finally	---> Used with exceptions, a block of code that will be executed no matter
             if there is an exception or not
for    --->  To create a for loop
from   --->  To import specific parts of a module
global --->  To declare a global variable
if	---> To make a conditional statement
import	---> To import a module
in      ---> To check if a value is present in a list, tuple, etc.
is	---> To test if two variables are equal
lambda	---> To create an anonymous function
None	---> Represents a null value
nonlocal---> To declare a non-local variable
not	---> A logical operator
or	---> A logical operator
pass	---> A null statement, a statement that will do nothing
raise	---> To raise an exception
return	---> To exit a function and return a value
True    ---> Boolean value, result of comparison operations
try	---> To make a try...except statement
while	---> To create a while loop
with	---> Used to simplify exception handling
yield   ---> To end a function, returns a generator

------------------------------------------------------------------------------------------------------------------
2.== VS IS OPERATORS

  --> ==  : is for value equality. It's used to know if two objects have the same value.
  -->  is : is for reference equality. It's used to know if two references refer (or point) to the same object, i.e if they're identical.

------------------------------------------------------------------------------------------------------------------------------
3./ // % DIFFERENCES

    '/'  Division  --> Divides left hand operand by right hand operand

    '//' Floor Division	--> The division of operands where the result is the quotient in which the digits after the decimal point are removed.
                            But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) −

     '%' Modulus   -->	Divides left hand operand by right hand operand and returns remainder	

----------------------------------------------------------------------------------------------------------------------------------
         4.DECISION MAKING, LOOPS
===============================================



1.WHEN TO USE IF ELIF ELSE AND NESTEDIF
 
 A) if   --> python,if statement is used for decision making operations

    elif --> use the elif condition is used include multipleconditional expressions after the if condition or       
             b/w if and else conditions

    else -->  An if else Python statement evaluates whether an expression is true or false.
               If a condition is true, the “if” statement executes. Otherwise, the “else” statement executes

   nestedif --> There may be a situation when you want to check for another condition after a condition resolves to true

-------------------------------------------------------------------------------------------------------------------------------
2.WHILE VS FOR

       While loop – This loop statement checks for a condition at the beginning and till the condition is fulfilled, 
                    it will execute the body of the loop.

       For loop – For loops are used to sequentially iterate over a python sequence.
                  When the sequence has been iterated completely, the for loop ends and thus executes the next piece of code.

-------------------------------------------------------------------------------------------------------------------------------
                      5.DATA TYPES
          ======================================
1.DATA TYPES IN PYTHON

 A) 1.NUMBERS ---> python supports four different data types .they are int,long,float,comolex

    2.STRING ---> strings are amongst the most popular type in python.we can create them simply enclosing charecters in quotes
                  python threats single quotes the same as double quotes.

----------------------------------------------------------------------------------------------------------------------------
2.DATA STRUCTURES IN PYTHON

    list,tuple,dictionary and set

    list ----> list is a mutable data structure
               the list is a most versatile data type available in python which can be 
               written as a list of comma separated values b/w square brackets

    tuple ----> tuple is immutable data structure 
                tuples are sequences , just like lists

    dictionary ----> dictionary is a mutable data structure 
                    dictionary in python is an unorderd collection of data values

    set ----> a set is an unodered and mutable collection of unique elements

--------------------------------------------------------------------------------------------------------------------
3.SEQUENCES IN PYTHON

    In Python programming, sequences are a generic term for an ordered set which means that the order in which 
    we input the items will be the same when we access them.Python supports six different types of sequences. 
    These are strings, lists, tuples, byte sequences, byte arrays, and range objects.

----------------------------------------------------------------------------------------------------------------------------
4.CRUD OPERATIONS

     The abbreviation CRUD expands to Create, Read, Update and Delete. These four are fundamental operations in a database.
     In the sample database, we will create it, and do some operations
--------------------------------------------------------------------------------------------------------------------------
5.HTTP REQUEST METHODS.EXPLAIN IN DETAIL

     HTTP Methods
     GET
     POST
     PUT
     HEAD
     DELETE
    PATCH
    OPTIONS

  The two most common HTTP methods are: GET and POST.

     GET Method --> GET is used to request data from a specified resource.
                    GET is one of the most common HTTP method
                     
     POST Method --> POST is used to send data to a server to create/update a resource.
   
     PUT Method --> PUT is used to send data to a server to create/update a resource.

     HEAD Method --> HEAD is almost identical to GET, but without the response body.

     DELETE Method --> The DELETE method deletes the specified resource.

     PACTH Method --> Patch is used to modify the capabilities

     OPTIONS Method --> The OPTIONS method describes the communication options for the target resource.

-------------------------------------------------------------------------------------------------------------

VI. Data Structures:
----------------------
1.mutable vs immutable.explain in datail with all examples?

	-Mutable is a type of variable that can be changed. A mutable object is an object whose state can be modified after it is created.
 
	-Immutables are the objects whose state cannot be changed once the object is created. Strings and Numbers are Immutable.

	Examples:
	immutable : Numbers (int, float, bool,tuple, Strings)
	mutable  :list,set,dict

--------------------------------------------------------------------------------------------------------------------------------
2.sequence operations on each data structure?

	-A sequence is logically composed of three thingsan array of elements, a maximum number of elements that the array may contain, 
 	and a logical length indicating how many of the allocated elements are valid.
 -----------------------------------------------------------------------------------------------------------------------------------
 3.string why it is immutable.explain in details?

  	-strings are made immutable so that programmers cannot alter the contents of the object (even by mistake). 
	-This avoids unnecessary bugs. Some other immutable objects are integer, float, tuple, and bool.
------------------------------------------------------------------------------------------------------------------
list vs tuple?
list

	list is mutable
	implication of iterations is time- consuming
	list consume more memory
	list have several bulit in methods like append,count,extend,index,insert,reverse etc

tuple
	tuples are immutable
	The implication of iterations is comparatively faster
	tuple consume less memory as compared to the list
	tuple does not have many bulit in methods
      tuple functions like min,max,len etc
--------------------------------------------------------------------------------------------------- 
Append vs extend in list?
	-append adds its argument as a single element to the end of a list. The length of the list itself will increase by one.
	-extend iterates over its argument adding each element to the list, extending the list.
-------------------------------------------------------------------------
pop vs remove in list?

	-Python List remove() is an inbuilt function in the Python programming language that removes a given object from the List
	-Python list pop() is an inbuilt function in Python that removes and returns the last value from the List or the given index value. 

-------------------------------------------------------------------------------------------------------------------------
shallow copy and deep copy?

	-Shallow Copy reflects changes made to the new/copied object in the original object.
	-Deep copy doesn't reflect changes made to the new/copied object in the original object.

-----------------------------------------------------------------------------------------------------------------
9. Pass by reference vs pass by value
 
	--Passing by reference means the called functions' parameter will be the same as the callers' passed argument (not the value, but the identity - the variable itself). 
	--Pass by value means the called functions' parameter will be a copy of the callers' passed argument.

----------------------------------------------------------------------------------------------------------------------------------------------
10.dictionary methods
	
clear()	-	Removes all the elements from the dictionary
copy()	-	Returns a copy of the dictionary
fromkeys()	-	Returns a dictionary with the specified keys and value
get()		-	Returns the value of the specified key
items()	-	Returns a list containing a tuple for each key value pair
keys()	-	Returns a list containing the dictionary's keys
pop()		-	Removes the element with the specified key
popitem()	-	Removes the last inserted key-value pair
setdefault()-	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	-	Updates the dictionary with the specified key-value pairs
values()	-	Returns a list of all the values in the dictionary

------------------------------------------------------------------------------------------------------------------------------------
11.dictionary get method purpose

	-get() method is used in Python to retrieve a value from a dictionary. dict. get() returns None by default if the key you specify cannot be found. 
	-With this method, you can specify a second parameter that will return a custom default value if a key is not found.

---------------------------------------------------------------------------------------------------------------------------------------------------------------
12.Properties of - String

	 String is a collection of alphabets, words or other characters. It is one of the primitive data structures and are the building blocks for data manipulation.
	 Python has a built-in string class named str . Python strings are "immutable" which means they cannot be changed after they are created.

	capitalize()   	Converts the first character to upper case
	casefold()		Converts string into lower case
	center()		Returns a centered string
	count()		Returns the number of times a specified value occurs in a string
	encode()		Returns an encoded version of the string
	endswith()		Returns true if the string ends with the specified value
	expandtabs()	Sets the tab size of the string
	find()		Searches the string for a specified value and returns the position of where it was found
	format()		Formats specified values in a string
	format_map()	Formats specified values in a string
	index()		Searches the string for a specified value and returns the position of where it was found
	isalnum()		Returns True if all characters in the string are alphanumeric
	isalpha()		Returns True if all characters in the string are in the alphabet
	isascii()		Returns True if all characters in the string are ascii characters
	isdecimal()		Returns True if all characters in the string are decimals
	isdigit()		Returns True if all characters in the string are digits
	isidentifier()	Returns True if the string is an identifier
	islower()		Returns True if all characters in the string are lower case
	isnumeric()		Returns True if all characters in the string are numeric
	isprintable()	Returns True if all characters in the string are printable
	isspace()		Returns True if all characters in the string are whitespaces
	istitle()		Returns True if the string follows the rules of a title
	isupper()		Returns True if all characters in the string are upper case
	join()		Converts the elements of an iterable into a string
	ljust()		Returns a left justified version of the string
	lower()		Converts a string into lower case
	lstrip()		Returns a left trim version of the string
	maketrans()		Returns a translation table to be used in translations
	partition()		Returns a tuple where the string is parted into three parts
	replace()		Returns a string where a specified value is replaced with a specified value
	rfind()		Searches the string for a specified value and returns the last position of where it was found
	rindex()		Searches the string for a specified value and returns the last position of where it was found
	rjust()		Returns a right justified version of the string
	rpartition()	Returns a tuple where the string is parted into three parts
	rsplit()		Splits the string at the specified separator, and returns a list
	rstrip()		Returns a right trim version of the string
	split()		Splits the string at the specified separator, and returns a list
	splitlines()	Splits the string at line breaks and returns a list
	startswith()	Returns true if the string starts with the specified value
	strip()		Returns a trimmed version of the string
	swapcase()		Swaps cases, lower case becomes upper case and vice versa
	title()		Converts the first character of each word to upper case
	translate()		Returns a translated string
	upper()		Converts a string into upper case
	zfill()		Fills the string with a specified number of 0 values at the beginning
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
		- List
--------------------------------------------------------------------------------------------------------------------------
	a list is created by placing elements inside square brackets [] , separated by commas.
 	A list can have any number of items and they may be of different types (integer, float, string, etc.).
	append()	Adds an element at the end of the list
	clear()	Removes all the elements from the list
	copy()	Returns a copy of the list
	count()	Returns the number of elements with the specified value
	extend()	Add the elements of a list (or any iterable), to the end of the current list
	index()	Returns the index of the first element with the specified value
	insert()	Adds an element at the specified position
	pop()		Removes the element at the specified position
	remove()	Removes the first item with the specified value
	reverse()	Reverses the order of the list
	sort()	Sorts the list
----------------------------------------------------------------------------------------------------------------------------------------------------
		- Tuple
------------------------------------------------------------------------------------------------------------------------------------------

	Tuples are used to store multiple items in a single variable
	A tuple is a collection which is ordered and unchangeable.
	count()	Returns the number of times a specified value occurs in a tuple
        index()	Searches the tuple for a specified value and returns the position of where it was found
 
--------------------------------------------------------------------------------------------------------------------------------

		- Dictionary
----------------------------------------------------------------------------------------------------------------------------------------------

       Dictionary in Python is an unordered collection of data values, used to store data values like a map, which, unlike other Data Types that hold
       only a single value as an element,
       Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized.

   clear()	Removes all the elements from the dictionary
   copy()	Returns a copy of the dictionary
  fromkeys()	Returns a dictionary with the specified keys and value
   get()	Returns the value of the specified key
  items()	Returns a list containing a tuple for each key value pair
  keys()	Returns a list containing the dictionary's keys
    pop()	Removes the element with the specified key
  popitem()	Removes the last inserted key-value pair
 setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
   update()	Updates the dictionary with the specified key-value pairs
  values()	Returns a list of all the values in the dictionary

--------------------------------------------------------------------------------------------------------------------------------------
		- Set
---------------------------------------------------------------------------------------------------------------------------------------

  A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements. Python’s set class represents 
  the mathematical notion of a set.

   add()	Adds an element to the set
  clear()	Removes all the elements from the set
  copy()	Returns a copy of the set
  difference()	Returns a set containing the difference between two or more sets
  difference_update()	Removes the items in this set that are also included in another, specified set
   discard()	Remove the specified item
 intersection()	Returns a set, that is the intersection of two or more sets
 intersection_update()	Removes the items in this set that are not present in other, specified set(s)
 isdisjoint()	Returns whether two sets have a intersection or not
  issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
 pop()	Removes an element from the set
 remove()	Removes the specified element
 symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()  	Return a set containing the union of sets
 update()	Update the set with another set, or any other iterable

------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------
13.Collections module classes, properties

   - Default dict 
          Defaultdict is a container like dictionaries present in the module collections.
          Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object
         that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.

   - Ordered dict
         An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted

   - Named tuple
 
     Named tuples are tuples that allow their elements to be accessed by name instead of just index!
    You make a namedtuple like this: >>> from collections import namedtuple >>> Student = namedtuple('Student', ['first', 'last', 'grade'])

  - Frozen set 

      The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable.
      elements of the frozen set remain the same after creation.
      frozen sets can be used as keys in Dictionary or as elements of another set. But like sets, it is not ordered (the elements can be set at any index).

  - Counter
 
     Python Counter is a container that will hold the count of each of the elements present in the container. 

----------------------------------------------------------------------------------------------

14.Lambda function. Examples with map filter reduce functions

   --A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.
     Python map() applies a function on all the items of an iterator given as input. 
     An iterator, for example, can be a list, a tuple, a set, a dictionary, a string, and it returns an iterable map object. 

     The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
    reduce() is a function that implements a mathematical technique called folding or reduction. 
    reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value.
------------------------------------------------------------------------------
15.range vs xrange

     range() – This returns a range object (a type of iterable).
     xrange() – This function returns the generator object that can be used to display numbers only by looping.
     The only particular range is displayed on demand and hence called “lazy evaluation“.

    The xrange() function in Python is used to generate a sequence of numbers, similar to the range() function. 
    However, xrange() is used only in Python 2. x whereas range() is used in Python 3.
---------------------------------------------------------------------------------------------------
VII. OOPs:
------------------------------------------------------------------------------------------------
1. What is oops
	-Object Oriented programming (OOP) is a programming paradigm that relies on the concept of classes and objects.
	-It is used to structure a software program into simple, reusable pieces of code blueprints (usually called classes), 
 	which are used to create individual instances of objects
-----------------------------------------------------------------
2. What are oops features
	There are five important featurs related to oops.they are
	-classes and objects
	-Encapsulation
	-Abstraction
	-Inheritance
	-Polymorphism
-------------------------------------------------------------------------------------------
3. class vs object. Explain in detail
 
	-class contains variables and methods and also a class is a model or blueprint for creating objects
	-An object is simply a collection of data (variables) and methods (functions) that act on those data
--------------------------------------------------------------------------
4. Explain each feature in detail with examples

   a. Encapsulation

    Encapsulation is the process of wrapping up variables and methods into a single entity
    So, for example, when you create a class, it means you are implementing encapsulation.
    A class is an example of encapsulation as it binds all the data members (instance variables) and methods into a single unit.

   b. Abstraction

     abstraction “displays” only the relevant attributes of objects and “hides” the unnecessary details. For example, when we are driving a car, 
    we are only concerned about driving the car like start/stop the car, accelerate/ break, etc. ... This is a simple example of abstraction.

   c. Inheritance

     -Inheritance relationship defines the classes that inherit from other classes as derived, subclass, or sub-type classes.
      Base class remains to be the source from which a subclass inherits
    -The main advantage of inheritance is code reusability
     Ex: you have a Base class of “Animal,” and a “Lion” is a Derived class. The inheritance will be Lion is an Animal

 d. Polymorphism

 The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) 
 being used for different types.

-----------------------------------------------------------------

5. Method overloading. Explain in detail

  -- Methods in Python can be called with zero, one, or more parameters. 
     This process of caslling the same method in different ways is called method overloading. ...
     Two methods cannot have the same name in Python; hence method overloading is a feature that allows the same operator to have different meanings.

-------------------------------------------------------

6. Method overriding. Explain in detail
 
   -- Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a 
     specific implementation of a method that is already provided by one of its super-classes or parent classes

------------------------------------------------------------

7. Inheritance types.Explain in detail 

      Types of Inheritance:

         1). Single inheritance:-- When child class is derived from only one parent class. This is called single inheritance.
 
         2). Multiple inheritances:-- When a class is derived from more than one base class it is called multiple Inheritance. 
            The derived class inherits all the features of the base case.

        3). Multilevel inheritance:-- The multi-level inheritance includes the involvement of at least two or more than two classes.  
            One class inherits the features from a parent class and the newly created sub-class becomes the base class for another new class

       4). Hierarchical inheritance.-When we derive or inherit more than one child class from one(same) parent class. 
          Then this type of inheritance is called hierarchical inheritance.

       5). Hybrid inheritance:-- Hybrid inheritance is a combination of simple, multiple inheritance and hierarchical inheritance
------------------------------------------------------------------------------------------------------------------------------------------------
8. Abstraction Explain in detail

     ---- Abstraction:--  Abstraction in OOP is a process of hiding the real implementation of the method by only showing a method signature.
                          In Python, we can achieve abstraction using ABC (abstraction class) or abstract method. ABC is a class from the abc module in Python

-----------------------------------------------------------------------------------------------------
9. Abstract class vs interface 

   Abstract

      --- A class is called an Abstract class if it contains one or more abstract methods. An abstract method is a method that is declared, 
          but contains no implementation. Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasse

  Interface

    --- the interface is a collection of method signatures that should be provided by the implementing class. 
        Implementing an interface is a way of writing an organized code and achieve abstraction.

-------------------------------------------------------
10.Mulitple inheritance. MRO method resolution order priciple

   --- The Python Method Resolution Order defines the class search path used by Python to search for the right method 
       to use in classes having multi-inheritance

------------------------------------------------------------------------------
11. Diamond problem

    --- The diamond problem occurs when two classes have a common ancestor, and another class has both those classes as base classes
-------------------------------------------------------------------------
12. Constructor

    --- A constructor is a special method that is useful to declare and initialize the instance variables
       A constructor is a special kind of method that Python calls when it instantiates an object using the definitions found in your class. 
       Python relies on the constructor to perform tasks such as initializing (assigning values to) any instance variables 
       that the object will need when it starts.

--------------------------------------------------------------------
13. Constructor overloading

     --- Python does not support Constructor overloading; it has no form of function. 
         In Python, Methods are defined solely by their name, and there can be only one method per class with a given name.

--------------------------------------------------------------------------------------------------------
14. __init__ purpose
 
   --- init is short for initialization. It is a constructor which gets called when you make an instance of the class and it is not necessary.
       But usually it our practice to write init method for setting default state of the object.
 ----------------------------------------------------------------------------------------------------

12. Special functions 

    __init__ 

	-The __init__ function is called every time an object is created from a class. 
	-The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes

   __str__ 

      - The __str__ method in Python represents the class objects as a string – it can be used for classes. 
      - The __str__ method should be defined in a way that is easy to read and outputs all the members of the class.
        This method is also used as a debugging tool when the members of a class need to be checked.

   __repr__

      -- In Python, __repr__ is a special method used to represent a class's objects as a string. __repr__ is called by the repr() built-in function.
         You can define your own string representation of your class objects using the __repr__ method. 
         Special methods are a set of predefined methods used to enrich your classes.

    __iter__
  
     -- The Python iter() function returns an iterator for the given object. The iter() function creates an object which can be iterated one element at a time.
        These objects are useful when coupled with loops like for loop, while loop.
	   
   __next__

     -- The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration

------------------------------------------------------------------
13. access modifiers. Does exist in python.Explain in detail 

	-The access modifiers in Python are used to modify the default scope of variables. 
	-Three types of access modifiers:

  Public Access Modifier
	-The members of a class that are declared public are easily accessible from any part of the program.
	All data members and member functions of a class are public by default. 

  Protected Access Modifier
	-The members of a class that are declared protected are only accessible to a class derived from it.
	Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class. 

 Private Access Modifier
	-The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier. 
	Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class. 

---------------------------------------------------------------------------------

14. super keyword in python 
	-The super() function is used to give access to methods and properties of a parent or sibling class. 
	-The super() function returns an object that represents the parent class.

--------------------------------------------------------------------------------------
15. Access super class methods from sub class

---------------------------------------------------------
16. Class vs instance varaibles

  Class variables:

	-Class variables are also called static variables
	-Class variables are the variables whose single copy is available to all the instance of the class
	-Declared inside the class definition (but outside any of the instance methods). They are not tied to any particular object of the class, 
	hence shared across all the objects of the class. Modifying a class variable affects all objects instance at the same time.

  Instance Variables:

	-Instance variables are the variables whose seperate copy is created in every instance(or object)
	-Instance variables are referenced as instancename.var
	-Declared inside the constructor method of class (the __init__ method). They are tied to the particular object instance of the class, 
	hence the contents of an instance variable are completely independent from one object instance to the other.
--------------------------------------------------------------

17. class method vs instance method vs static method
 
  Class Method:

	-A class method can not access data from any specific instance or object. It can access any class variable or static method.
	-The class method defines the behavior of the class.
	-The class method takes cls (class) as first argument.
	-The class method takes the class as parameter to know about the state of that class.
	-To define a class method in python, we use @classmethod decorator

  Instance Method:

	-The instance method defines the behavior of the object (instance)
	-Instance methods are the methods which act upon the instance variables of the class.
	-Instance method use self as first default parameter
	-Instance method are methods which require an object of its class to be created before it can be called. To invoke a instance method, 
	we have to create an Object of the class in which the method is defined

Static Method:
	-The static method does not take any specific parameter.
	-Static Method cannot access or modify the class state.
	-Static methods do not know about class state. These methods are used to do some utility tasks by taking some parameters.
	-to define a static method we use @staticmethod decorator.
 
--------------------------------------------------------------
18. self importance 

	-self is a default variable that contains the memory address of the instance of the current class.
	-we need not pass anything to variable
	-self variable becomes the first parameter for constructor and instance method
	-The self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python.

-------------------------------------------------------

VIII. Packages, Modules:

------------------------------------------------------------------------------------------------
1. package vs module
	-The package is a simple directory having collections of modules. This directory contains Python modules and also having __init__.py file by which the 
	interpreter interprets it as a Package. The package is simply a namespace. The package also contains sub-packages inside it.

	-The module is a simple Python file that contains collections of functions and global variables and with having a .py extension file. 
	It is an executable file and to organize all the modules we have the concept called Package in Python.

-------------------------------------------------------------------------------
2. scope resolution 

    Scope resolution in Python follows the LEGB rule.

       -- L, Local — Names assigned in any way within a function (or lambda), and not declared global in that function.

       -- E, Enclosing-function locals — Name in the local scope of any and all statically enclosing functions(or lambdas), from inner to outer.

       -- G, Global (module) — Names assigned at the top-level of a module file, or by executing a global statement in a def within the file.

       -- B, Built-in (Python) — Names preassigned in the built-in names module : open, range,SyntaxError, etc.
-------------------------------
3. recursive import issue
---------------------
4. different libraries used in your project. Explain each one 
 json
	-It is the string version that can be read or written to a file. Python has a JSON module that will help converting the datastructures to JSON strings. 
	-The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.
gzip
	-Python's gzip module is the interface to GZip application. The gzip data compression algorithm itself is based on zlib module.
 	-The gzip module contains definition of GzipFile class along with its methods. It also caontains convenience function open(), compress() and decompress().

csv
	-CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database.
	- A CSV file stores tabular data (numbers and text) in plain text. Each line of the file is a data record.

xwlt
	-This is a library for developers to use to generate spreadsheet files compatible with Microsoft Excel versions 95 to 2003.
 	The package itself is pure Python with no dependencies on modules or packages outside the standard Python distribution.

base64
	-base64 module is used to encode and decode data. First, the strings are converted into byte-like objects and then encoded using the base64 module. 
	-The below example shows the implementation of encoding strings isn't base64 characters. Example: import base64.

os
	-The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc. ...
 	-You first need to import the os module to interact with the underlying operating system

sys
	-The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment.
 	-It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter.

sentry	
	-Sentry's Python SDK enables automatic reporting of errors and exceptions as well as identifies performance issues in your application.
 	-Sentry's Python SDK includes powerful hooks that let you get more out of Sentry, and helps you bind data like tags, users, or contexts.	
flask
	-Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications
  	-Flask is a micro web framework written in Python. ... Extensions exist for object-relational mappers, form validation, upload handling, various 
	open authentication technologies and several common framework related tools
flask_restful
random 
	-Python Random module is an in-built module of Python which is used to generate random numbers. These are pseudo-random numbers means these are not truly random.
 	-This module can be used to perform random actions such as generating random numbers, print random a value for a list or string, etc.			
request
	-The requests module allows you to send HTTP requests using Python.
	-The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).
requests
	-Requests is a Python Library that lets you send HTTP/1.1 requests,
	 add headers, form data, multipart files, and parameters with simple Python dictionaries. It also lets you access the response data in the same way.
   pickle 
  -----------------------
5. Serialization deserialization:
	-Object serialization is the process of converting state of an object into byte stream. This byte stream can further be stored in any file-like object such as a disk file or memory stream. It can also be transmitted via sockets etc.
 	-Deserialization is the process of reconstructing the object from the byte stream.
  	 
	-Pickling is the process whereby a Python object hierarchy is converted into a byte stream, 
	-unpickling is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.
   
	-load() is used to read the JSON document from file and The json.
	- loads() is used to convert the JSON String document into the Python dictionary.
	-The json. dump() method (without “s” in “dump”) used to write Python serialized object as JSON formatted data into a file.
	- The json. dumps() method encodes any Python object into JSON formatted String
-------------------------------------------------------------------------------------------------------------------------------------------

            Exception Hadling:
-------------------------------------------------------------------------------------------------------------------------------------
1. Why we need to do exception hanlding

	-Python provides a way to handle the exception so that the code can be executed without any interruption. 
	-If we do not handle the exception, the interpreter doesn't execute all the code that exists after the exception.

-----------------------------------------------
2. Exception class hierarchy

	-The Python exception class hierarchy consists of a few dozen different exceptions spread across a handful of important base class types. ... 
	This allows our code to explicitly catch or rescue the raised exception and programmatically react to it in an appropriate manner.

---------------------------------------------------------------------------------------------------

3. try except else finally. Explain in detail.

	-The try block lets you test a block of code for errors.

	-The except block lets you handle the error.

	-The else block lets you execute code when there is no error.

	-The finally block lets you execute code, regardless of the result of the try- and except blocks. 

-----------------------------------------------------------------------
4. how to handle mulitple exceptions

	-You can also handle multiple exceptions using a single except clause by passing these exceptions to the clause as a tuple .
 	Finally, you can also leave out the name of the exception after the except keyword

-------------------------------------------------------------------------
5. exception hierarchy 

	-The Python exception class hierarchy consists of a few dozen different exceptions spread across a handful of important base class types. ... 
	While a fatal error will halt execution of the current application, all non-fatal exceptions allow execution to continue.

-------------------------------------------------------------------------------
IX. File handling:
------------------------------------------------------------------------------------------------
1. Different file handling operations

	r	Opens a file for reading. (default)
	w	Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
	x	Opens a file for exclusive creation. If the file already exists, the operation fails.
	a	Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
	t	Opens in text mode. (default)
	b	Opens in binary mode.
	+	Opens a file for updating (reading and writing)
  
-----------------------------------------------------

2. open function how to use

	-The python open() function is used to open() internally stored files. It returns the contents of the file as python objects.

-----------------------------------------------------
3. Context manager in python. How it works internally

	-Context managers allow you to allocate and release resources precisely when you want to. The most widely used example of context managers is the with statement.
	 Suppose you have two related operations which you'd like to execute as a pair, with a block of code in between.

---------------------------------------------------------------

4. __enter__ vs __exit__ methods 
	__enter__ method is called at the start of with block 
 	__exit__ method is called at the end. 
	Note: with statement only works with objects that support the context management protocol (i.e. they have __enter__ and __exit__ methods). 
	 A class which implement both methods is known as context manager class
--------------------------------------------------------------------------------------------------------------
X. Iterator,Generator:
--------------------------
1. Iterator protocol in python 

	-The iterator protocol defines a standard way to produce a sequence of values (either finite or infinite), and potentially a return value when all values have been generated.
 	An object is an iterator when it implements a next() method with the following semantics: Property. Value. next()
-------------------------------------------------------------
2. Generator protocol in python 

	-Python provides a generator to create your own iterator function. A generator is a special type of function which does not return a single value, instead, it returns an iterator object with a sequence of values.
 	In a generator function, a yield statement is used rather than a return statement.
---------------------------------------------------
3. Iterator vs generator

	Iterators: Iterator are objects which uses next() method to get next value of sequence.
 	Generators: A generator is a function that produces or yields a sequence of values using yield method.

	iter() keyword is used to create an iterator containing an iterable object.
	next() keyword is used to call the next element in the iterable object.

XI. Decorator:
-------------------
1. What is decorator

	-it allows programmers to modify the behaviour of function or class.
 	-Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
------------------------------------------------------------------------
2. Different decorators.Explain in detail
  
   @classmethod
	-the @classmethod decorator is used to declare a method in the class as a class method that can be called using ClassName. MethodName() . 
	-The class method can also be called using an object of the class. The @classmethod is an alternative of the classmethod() function.

  @staticmethod
	-Static methods, much like class methods, are methods that are bound to a class rather than its object. They do not require a class instance creation.
 	  So, they are not dependent on the state of the object. ... Class method works with the class since its parameter is always the class itself.

  @property
       -Python property() function returns the object of the property class and it is used to create property of a class.  
	  Syntax: property(fget, fset, fdel, doc)

  @abstractmethod
	-abstractmethod(function) A decorator indicating abstract methods. Using this decorator requires that the class's metaclass is ABCMeta or is derived from it.
 	A class that has a metaclass derived from ABCMeta cannot be instantiated unless all of its abstract methods and properties are overridden
-----------------------------------------
3. How decorator works internally.

 	-decorators work as wrappers, modifying the behavior of the code before and after a target function execution, without the need to modify the function itself, 
	augmenting the original functionality, thus decorating it
-------------------------------------------
4. Why we need to use decorator
	-A decorator in Python is a function that takes another function as its argument, and returns yet another function . 
	-Decorators can be extremely useful as they allow the extension of an existing function, without any modification to the original function source code.

XII. Python 2.x vs 3.x 
-------------------------
	-In python 2. x, “print” is treated as a statement 
	-python 3. x explicitly treats “print” as a function. 
	-This means we need to pass the items inside your print to the function parentheses in the standard way otherwise you will get a syntax error

	-Python 3 syntax is simpler and easily understandable whereas Python 2 syntax is comparatively difficult to understand. 
	-Python 3 default storing of strings is Unicode whereas Python 2 stores need to define Unicode string value with “u.


XIII. Regular Expressions:
-------------------------------
      -- A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
         RegEx can be used to check if a string contains the specified search pattern.

XIV. Networking:
------------------

XV. Datetime:
-----------------

XVI. Database interaction:
-----------------------------


