'''
https://www.brainfuse.com/jsp/alc/resource.jsp?s=gre&c=35234&cc=108822
https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:foundation-algebra
'''
'''
Java:
-------
int x; # Declaration
x = 10 # initialize

int x = 10;

Python:
--------
x = 10


Expression : An expression is a number, a variable, 
             or a combination of numbers, variables and operation symbols.
             Ex: 4.5 + 1 <==>  5.5
                 2x + 3
                  
Equation   : Equation is made up of two expressions connected by an equal sign.
             Ex: 16 - 6 = 10
                 x + 8  = 40
                 3x + 4 = 5x + 14
                 L.H.S  = R.H.S     = vs == 
                 


Numeric expression   : It will contain all numbers.
                       To apply operations to numbers we can use this
                       Ex: 2(3 + 8) 
                           = 6 + 8 
                           = 14
                       
Algebraic expression : At least one variable and at least one operation
                       Ex: 2(x + 8y)

3x+4y 

 3(4x+5y)-2(3x-7y) :   x = 10 y = 20        - Substitute and then get value
 3(4x+5y)-2(3x-7y) :   x = 2/43 y = 54/533  - Simplify, then substitute and get value
 
PROBLEM :
----------
Simplify the algebraic expression: 3(4x+5y)-2(3x-7y)

Then evaluate the simplified expression for x = 3 and y = -2.
            ==> I. Substitute the values, get final output

Then evaluate the simplified expression for x = 2/7 and y = 3/4.
            ==> II. Simplify the expression, then substitute the values 

Solution:
--------
Step 1: Simplify the algebraic expression using the basic properties of real numbers.
        = 3(4x+5y) - 2(3x-7y)
        = 3(4x+5y) + (-2)(3x+[-7]y)   <==  Definition of Subtraction
        = 12x + 15y + (-6)x + 14y     <==  Distributive property
        = 12x + (-6)x + 15y + 14y     <== Commutative property of Addition
        = (12+[-6])x + (15 + 14)y     <== Distributive property
        = 6x + 29y                    <== Simplify

Step 2: Now subustitute x with 3 and y with -2
        = 6(3) + 29(-2)
        = -40
        
PROBLEM :
----------        
Prove (a+b)?? = a??+2ab+b??

Solution:
---------
Here LHS = (a+b)??
     RHS = a??+2ab+b??


(a+b)??  = (a+b)??(a+b)
        
        = (a+b)(a+b)
        
        = [a??(a+b)]+[b??(a+b)]
        
        = [a(a+b)]+[b(a+b)]
        
        = [{(a??a)+(a??b)}] + [{(b??a)+(b??b)}]
        
        = [(a??)+(ab)] + [(ba)+(b??)]
        
        = (a??)+(ab)+(ba)+(b??)
        
        = (a??)+(ab)+(ab)+(b??)   <== Since a??b = b??a (commutative property), ba = ab.
        
        = (a??)+(2??ab)+(b??)
        
        = a??+2ab+b??
        
        = RHS

 ???  LHS = RHS
 Hence Proved

'''