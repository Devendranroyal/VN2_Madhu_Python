'''
'''
'''
https://global.gotomeeting.com/#/meetings/anytime-meetings
https://www.amazon.in/ap/signin

         Client         --      Server
        Local browser           USA, Remote machine 
       www.amazon.com   ----->  162.219.225.118
                    <--login page---
3 points:
---------
1. Request URL 
2. Request Method
3. Payload

II. HTTP Request methods : GET POST PUT DELETE 
-------------------------------------------
GET  - to retrieve data from server     --- "My " Amazon
                                            display items
POST - to create the data into server   --- Signup 
PUT  - to update the resource(data)     --- Change delivery address 
                                            Change password 
DELETE - to delete the resource         --- account deactivate 
                                        --- cancel the order 
                                        --- delete item in cart 
                                        
III. Payload: 
--------------
Login :   {'username':'nettemmadhu',
          'password':'pass'
          }     
          json format 
          pickling unpickling 
          serialization deserialization
          json.loads() dumps() 
                                           
Signup:  {"username,paswwor,mobile,gender,locaiotn,......}
 
MyOders : GET /api/v1/getdata/21321321 
 
 
https://www.javatpoint.com/                  - Home pagae


Click on Python button in home page 

API CALL   :
--------------
Request URL    : https://www.javatpoint.com/python-tutorial
Request Method : GET
Payload        : NA


Status Code: 200 
content-type: text/html
path: /python-tutorial
scheme: https 



'''
'''
Website: https://www.amazon.in/ap/signin?_encoding=UTF8&accountStatusPolicy=P1&openid.assoc_handle=inamazon&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Forder-history%3Fie%3DUTF8%26ref_%3Dnav_orders_first&pageId=webcs-yourorder&showRmrMe=1
protocol          : https
domain            : www.amazon.com
suffix url/path   : ap/signin
query parameteres : _encoding=UTF8 &
                    accountStatusPolicy=P1 & 
                    openid.assoc_handle=inamazon & 
                    openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select
                    &openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Forder-history%3Fie%3DUTF8%26ref_%3Dnav_orders_first&pageId=webcs-yourorder&showRmrMe=1

'''
# 1. Request URL
import urllib.parse
url = "https://www.google.com/search?q=networking+layers+osi+model&rlz=1C1CHBF_enIN835IN835&sxsrf=ALeKk00dGqHArXquUobMFYDOxdbP70oLyA:1612842660470&tbm=isch&source=iu&ictx=1&fir=Bd81XnzZHgtTUM%252CF2v0ZXThlQYD6M%252C_&vet=1&usg=AI4_-kQeiCZ0WfIXRJx3r0ep8aDwX_M76A&sa=X&ved=2ahUKEwj7hOyO89vuAhXmxDgGHQdEDQ4Q9QF6BAgLEAE&biw=1517&bih=694#imgrc=hYHggnMXACIXNM"
# Get tuple with parts of url
tup = urllib.parse.urlparse(url)

# Display contents of tuple
print(tup)
print("Scheme : ", tup.scheme)
print("Netloc : ", tup.netloc)
print("Path,suffix url   : ", tup.path)
print("Params : ", tup.params)
print("Port   : ", tup.port)
print("URL    : ", tup.geturl())

'''
2. Request Method:

HTTP Request methods :
--------------------------
GET -- for data retrieval      --- R ETRIEVAL
POST -- to save data           --- C REATE
PUT --- to update the record   --- U PDATE
DELETE --- to delete the record -- D ELETE

Request URL     : https://digitalcatalog.paytm.com/dcat/v1/category/17/getcategory?channel=web&version=2&child_site_id=1&site_id=1&locale=en-in
                  https://
                  digitalcatalog.paytm.com
                  /dcat/v1/category/17/getcategory ? 
                      channel=web&
                      version=2&
                      child_site_id=1&
                      site_id=1&
                      locale=en-in
Request Method  : GET
Payload         : 

API Specification/call/details :
=================================
Request URL    : http://amazon.com/signupuser  /signupuser
Request Method : POST
Payload        : {'name':'MadhuNettem',
                  'email':"nettemmadhu@gmail.com',
                  'password':'123456',
                  'mobileno':'74023123213'
                  }

json vs dict 
json to dict conversion in python
dict to json conversion in python

json.loads()  load()
json.dumps()  dump()
pickle 

xml to python dict 
dict to xml 


'''