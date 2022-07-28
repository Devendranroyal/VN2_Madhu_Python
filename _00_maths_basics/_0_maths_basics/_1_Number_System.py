'''
https://www.mathsisfun.com/unit-conversion-tool.php
https://www.mathsisfun.com/unit-conversion-tool.php
#
'''
'''
Number System <==> Data types


Integer Whole Fractional Real  Imaginary   ==> Data Types     ===> int float boolean String
Sets, Sequences, Matrices                  ==> Data Structures ==> List Tuple Dictionary Set
'''
'''
Number System
=====================
                    NUMBERS
Natural     Whole       Integer     Rational        Irrational
             - Even nos
             - Odd nos
             - Prime nos
             - Composite nos

Natural Numbers : 1,2,3,4,5.....
Whole Numbers   : 0,1,2,3,4.....  0 + natural numbers
                      Even  : 2,4,6,8,10....
                      Odd   : 1,3,5,7,9.....
                      Prime : 2,3,5,7,11....
                      Comp  : 4,6,8,9,12....
Integers*       : {......-3,-2,-1,0,1,2,3,......}   ==> int *
Decimal*        : 12.3, 54.32, -34.432              ==> float *
Rational        : 2/3, 3/5 --> 0.6, -2/7
Irrational      : π, √3, √5 
Real nos        : Rational + Irrational
Imaginary nos*  : 3i+4j                              ==> complex
                        # 3 realno # 4 imaginaryno

CONCEPT:
----------------                 MATHS                 PYTHON
int decimal                 ==>  Number System    ===> Data Types (int float bool)
Sets, Sequences, Matrices   ==>  Adv topics       ===> Data Structures(String, List, Tuple, Dictionary, Set)


DATA TYPES/ STRUCTURES :
========================
==>Data types --> Individual values 
    --> Number system   int*    (100, 120) 
                        float*  (14.3,25.4)
                        complex  3i+4j
    --> Boolean         True/False   1/0       
    
==>Data structures --> Collection(Group) of individual values 
                       Maths: Sets Sequences Matrices      
                   --> String, List, Tuple, Dictionary, Set       


Conversion in mathematics :
---------------------------
Conversion : Measurement: to change from one unit to another 
                          such as from inches to millimeters, or liters to gallons

Temperature:
°C	  °F	Description
37	98.6	Body temperature

Length:
            1 km = 1000 m
            1 m  = 100 cm
            1 cm = 10 mm    ==> 1KM + 100M ==>  1KM + 0.1KM = 1.1 KM   Internal conversion(Same category)
                                               1000M + 100M = 1100 M
                                           ==> 100KM + 10M - 100.01KM
 
Mass:
            1 tonne = 1000 kg
            1 kg    = 1000 gm
            1 gm    = 1000 mg
            1 mg    = 0.0154 grain


            
Volume/Capacity:
            1 liter = 2.113 fluid pt
 
2 Dozen + 5 Dozen = 7 Dozen
5 KG + 3 KG = 8 KG 
3L water + 5L Oil = 8L
    - Calculate quantity ? YES - 8L
    - Mixture               NO - ERROR

Requiremnt : Combine Soda and Whisky 
             1L Soda + 30ML Whisky
                Usecase: Find quantity : YES :  1.03L  
                         Mixture       : YES :  Output



2 Dozen eggs + 5 KG Rice + 3L Water + 1 KM  ==> XXX Invalid statement 




1KM + 100M  ==> 1 KM + 0.1 KM ==> 1.1 KM
            ==> 1000 M + 100 M  ==> 1100 M
            
200KM + 5M = ......

int x = 10     # YES
float x = 10.5 # YES
float x = 10   # YES   10.0                   - Implicit casting
int x = 10.4   #  NO   int x = (int)10.4      - Explicit casting

'''