''''''


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

UI         ----->   Controller ---> Service  ---> DAO   ---> Database
           <-----              <---          <---       <---


    Part I                     Part II           Part III
    UI                        --> PL        ---> Database
    (HTML,CSS,Javascript)        (Python)        (Mysql, Postgresql, Mongodb)

UI --1-->                    Python                                   ----> Database
         --2.1-->  Controller  --2.2-->  Service  --2.3-->  DAO -->
         <--3.3--              <--3.2--             <--3.1--       <--

Layer Responsibilities:
     I. Controller --> Receive input from customer(UI), validate it.
    II. Service    --> Implement business logic
   III. DAO        --> Prepare query and interact with database,get results
   

Controller   :
---------------
     1. Receive the request data from UI,     (json,xml to dict) 
   2.1. Perform server side validations and
         if success: Pass the data to Service layer
         else      : Send error response  to UI
   2.2. Pass the data to Service layer
     3. Receive response from Service layer 
     4. Prepare resp data and send to UI

Service   :
---------------
     1. Receive the validated data from Controller
     2. Implement business logic as per give requirement
        If required interact with database for more data (dao layer call)
     4. Call dao layer(Pass the data) for data persistence
     5. Get response from DAO and send it to controller
  
  
DAO  Data Access Object: 
                1. Receive the data from service
                2. Get db connection,cursor etc.,
                3. Prepare and execute the sql query with data 
                4. Send response to Service
         
'''



