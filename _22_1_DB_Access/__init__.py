'''
Created on Sep 25, 2021
'''
import psycopg2   # pip install psycopg2
# c:\users\<lname>\appdata\local\programs\python\python39\lib\site-packages
'''
Desktop / Web / Enterprise Applications

Enterprise Application :  hdfc icici paytm
========================
  UI           ---   Backend                         --- Database
  ==========================================================================
  HTML               Python(Flask/Django/Fast API)      Postgresql* (RDBMS*)
  JavaScript         Java  (Spring,Struts,JSF)          MySQL*
  CSS                .Net                               Sqlite
  Angular            PHP                                Oracle/SQL Server
  React                                                 MongoDB* / Cassandra  (Nosql*)
'''
# Step1 : Get connection
# Step2 : Get cursor on db connection
# Step3 : Prepare SQL Query
# Step4 : Execute SQL query
# Step5 : Commit the transaction

try:
        # STEP 1 : Get connection
    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            database="postgres",
                            user="postgres",
                            password="vn2"
                            )
    print("Connection type :", type(conn))  # connection
    
        # STEP 2 : Get cursor on db connection
    cur = conn.cursor()  # cursor
    print("Connection type :", type(cur))
    
        # STEP 3 : Prepare SQL Query
    query = "create table DEPT_002(deptno INT,dname TEXT,loc text)"
    
        # STEP 4 : Execute SQL query
    cur.execute(query)
        # STEP 5 : Commit the transaction
    conn.commit()
    print("Table created successfully")
except Exception as ex:
    print("Exception occured during db transaction : ", ex)
finally:
    cur.close()
    conn.close()

'''
In postgresql db with DBeaver Tool, implement this below setup.


Execute below commands in postgresdb and start working on db questions.

Create DEPT Table:
==================
- create table dept(deptno INT,  dname TEXT,  loc TEXT)
     select * from dept
- ALTER TABLE DEPT ADD PRIMARY key  (deptno);
- select * from DEPT
        insert into DEPT (DEPTNO, DNAME, LOC) values(10, 'ACCOUNTING', 'NEW YORK')
        insert into dept values(20, 'RESEARCH', 'DALLAS')
        insert into dept values(30, 'SALES', 'CHICAGO')
        insert into dept values(40, 'OPERATIONS', 'BOSTON')
- select * from DEPT

Create EMPLOYEE Table:
==================
create table EMPLOYEE(empno INT,
                      ename TEXT,  
                      job TEXT,
                      mgr INT,
                      hiredate DATE,
                      sal INT,
                      comm INT,
                      deptno INT,
                      primary key(empno),  
                      foreign key(deptno) references dept(deptno)
                     )
select * from EMPLOYEE

insert into EMPLOYEE values(7839, 'KING', 'PRESIDENT', null, to_date('17-11-1981','dd-mm-yyyy'),5000, null, 10)
insert into EMPLOYEE values(7698, 'BLAKE', 'MANAGER', 7839,  to_date('1-5-1981','dd-mm-yyyy'), 2850, null, 30)
insert into EMPLOYEE values(7782, 'CLARK', 'MANAGER', 7839, to_date('9-6-1981','dd-mm-yyyy'), 2450, null, 10  )
insert into EMPLOYEE values(7566, 'JONES', 'MANAGER', 7839,  to_date('2-4-1981','dd-mm-yyyy'),2975, null, 20  )
insert into EMPLOYEE values(7788, 'SCOTT', 'ANALYST', 7566,  to_date('18-4-1987','dd-mm-yyyy') ,3000, null, 20 )
insert into EMPLOYEE values(7902, 'FORD', 'ANALYST', 7566,  to_date('3-12-1981','dd-mm-yyyy'),  3000, null, 20 )
insert into EMPLOYEE values(7369, 'SMITH', 'CLERK', 7902,  to_date('17-12-1980','dd-mm-yyyy'),  800, null, 20  )
insert into EMPLOYEE values(7499, 'ALLEN', 'SALESMAN', 7698,  to_date('20-2-1981','dd-mm-yyyy'),  1600, 300, 30 )
insert into EMPLOYEE values(7521, 'WARD', 'SALESMAN', 7698,  to_date('22-2-1981','dd-mm-yyyy'),  1250, 500, 30 )
insert into EMPLOYEE values(7654, 'MARTIN', 'SALESMAN', 7698,  to_date('28-9-1981','dd-mm-yyyy'),  1250, 1400, 30 )
insert into EMPLOYEE values(7844, 'TURNER', 'SALESMAN', 7698,  to_date('8-9-1981','dd-mm-yyyy'),  1500, 0, 30  )
insert into EMPLOYEE  values(7876, 'ADAMS', 'CLERK', 7788,  to_date('21-05-1987', 'dd-mm-yyyy'),  1100, null, 20  )
insert into EMPLOYEE  values(7900, 'JAMES', 'CLERK', 7698,  to_date('3-12-1981','dd-mm-yyyy'),  950, null, 30  )
insert into EMPLOYEE  values(7934, 'MILLER', 'CLERK', 7782,  to_date('23-1-1982','dd-mm-yyyy'),  1300, null, 10 )

1. RETRIEVAL Operations :
-------------------------
1. Write a query in SQL to display all the information of the employees.
2. Write a query in SQL to find the salaries of all employees
3. Write a query in SQL to display the unique designations for the employees.
4. Write a query in SQL to list the emp_name and salary is increased by 15%
5. Write a query in SQL to produce the output of employees name and job name as a fromat of "Employee & Job".
6. Write a query in SQL to produce the output of employees as follows.     Employee  JONAS(manager).
7. Write a query in SQL to list the employees with Hire date in the format like February 22, 1991
8. Write a query in SQL to count the no. of characters with out considering the spaces for each name.
9. Write a query in SQL to list the emp_id,salary, and commission of all the employees.
10. Write a query in SQL to display the unique department with jobs.
11. Write a query in SQL to list the employees who does not belong to department 2001
12. Write a query in SQL to list the employees who joined before 1991
13. Write a query in SQL to display the average salaries of all the employees who works as ANALYST.
14. Write a query in SQL to display the details of the employee BLAZE.
15. Write a query in SQL to display all the details of the employees whose commission is more or less than their salary.
16. Write a query in SQL to list the employees whose salary is more than 3000 after giving 25% increment.
17. Write a query in SQL to list the name of the employees, those having six characters to their name.
18. Write a query in SQL to list the employees who joined in the month January.
19. Write a query in SQL to list the name of employees and their manager separated by the string 'works for'.
20. Write a query in SQL to list all the employees whose designation is CLERK.
21. Write a query in SQL to list the employees whose experience is more than 27 years.
22. Write a query in SQL to list the employees whose salaries are less than 3500.
23. Write a query in SQL to list the name, job_name, and salary of any employee whose designation is ANALYST.
24. Write a query in SQL to list the employees who have joined in the year 1991.
25. Write a query in SQL to list the name, id, hire_date, and salary of all the employees joined before 1 apr 91
26. Write a query in SQL to list the employee name, and job_name who are not working under a manager.
27. Write a query in SQL to list all the employees joined on 1st may 91
28. Write a query in SQL to list the id, name, salry, and experiences of all the employees working for the manger 68319.
29. Write a query in SQL to list the id, name, salary, and experience of all the employees who earn more than 100 as daily salary
30. Write a query in SQL to list the employees who are retiring after 31-Dec-99 after completion of 8 years of service period.

For more programs, Refer - https://www.w3resource.com/sql-exercises/employee-database-exercise/index.php

Practice other scenarios as mentioned in below topics.

1 Introduction
2 Retrieve data from tables
3 Boolean and Relational Operators
4 Wildcard and Special operators
5 Aggregate Functions
6 Formatting query output
7 Query on Multiple Tables
8 SQL JOINS
9 SUBQUERIES

'''