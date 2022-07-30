# VN2_Madhu_Python

------------------------------------------------------------------------------------------------------------------------------------------
DJANGO 
------------------------------------------------------------------------------------------------------------------------------------------
Q)django is a web frame work

o


Q) Explain Django Architecture?

  ----- Django follows the MVT (Model View Template) pattern which is based on the Model View Controller architecture. 
  ----  It’s slightly different from the MVC pattern as it maintains its own conventions, so, the controller is 
        handled by the framework itself. 
        The template is a presentation layer. It is an HTML file mixed with Django Template Language (DTL). 
        The developer provides the model, the view, and the template then maps it to a URL, and finally, 
		Django serves it to the user.

==========================================================================================================================================

Q) Explain the django project directory structure?

  ------ manage.py    -  A command-line utility that allows you to interact with your Django project
 ------ __init__.py   -  An empty file that tells Python that the current directory should be considered as a Python package
 ------- settings.py  -  Comprises the configurations of the current project like DB connections.
 ------- urls.py      -  All the URLs of the project are present here
 ------- wsgi.py      -  This is an entry point for your application which is used by the web servers to serve
                         the project you have created.

=================================================================================================================================================

Q) What is Django Rest Framework(DRF)?

  ------ Django Rest Framework is an open-source framework based upon Django which lets you create RESTful APIs rapidly

===================================================================================================================================================

Q) What is Django ORM?

  ------- This ORM (an acronym for Object Relational Mapper) enables us to interact with databases in a more pythonic 
          way like we can avoid writing raw queries, it is possible to retrieve, save, delete and perform other operations over the database 
          without ever writing any SQL query. It works as an abstraction layer between the models and the database


Instead of creating tables at backend wfirst will create mdoel classes in modles.py 
and then will perofrmo makemigrations and migrate activities sot hat

ti will create tables at backend
we can iteract with db using model classes and in future even if we cahnge db we can direclty work with new db

without any chagnes at code level 


======================================================================================================================================================

Q) Explain what Flask is and its benefits?

     ------- Flask is a web microframework for Python based on “Werkzeug, Jinja2 and good intentions” BSD license. 
             Werkzeug and Jinja2 are two of its dependencies. This means it will have little to no dependencies on external libraries.  
             It makes the framework light while there is a little dependency to update and fewer security bugs.
    
    -------- A session basically allows you to remember information from one request to another.
             In a flask, a session uses a signed cookie so the user can look at the session contents and modify. 
             The user can modify the session if only it has the secret key Flask.secret_key.
============================================================================================================================================
Q)IS DJANGO BETTER THAN
nrh tvtrs
  -------Django and Flask map the URL’s or addresses typed in the web browsers to functions in Python. 
         Flask is much simpler compared to Django but, Flask does not do a lot for you meaning you will need to specify the details, 
         whereas Django does a lot for you wherein you would not need to do much work. Django consists of prewritten code,
         which the user will need to analyze whereas Flask gives the users to create their own code, therefore, making it simpler to understand the code.
         Technically both are equally good and both contain their own pros and cons.
===========================================================================================================================================================
Q) Mention the differences between Django, Pyramid and Flask.

    --------- Flask is a “microframework” primarily build for a small application with simpler requirements. 
             In flask, you have to use external libraries. Flask is ready to use.

    -------- Pyramid is built for larger applications.
            It provides flexibility and lets the developer use the right tools for their project. 
            The developer can choose the database, URL structure, templating style and more. Pyramid is heavy configurable.

   --------- Django can also be used for larger applications just like Pyramid. It includes an ORM.

==========================================================================================================================================================

Q) What are different model inheritance styles in the Django?
 
     Abstract Base Class Inheritance: Used when you only need the parent class to hold information that you don’t want to write for each child model.
 
    Multi-Table Model Inheritance:  Used when you are subclassing an existing model and need each model to have its own table in the database.

    Proxy Model Inheritance:  Used when you want to retain the model's field while altering the python level functioning of the model

===========================================================================================================================================================

Q). What is map function in Python?

    ------ map function executes the function given as the first argument on all the elements of the iterable given as the second argument.
           If the function given takes in more than 1 arguments, then many iterables are given. #Follow the link to know more similar functions.

====================================================================================================================================

Q). Is python numpy better than lists?

  -------- We use python numpy array instead of a list because of the below three reasons:

        Less Memory
        Fast
        Convenient
        For more information on these parameters, you can refer to this section – Numpy Vs List.
=========================================================================================================================================

Q)  What are models in Django?

  ------- A model in Django refers to a class that maps to a database table or database collection.
          Each attribute of the Django model class represents a database field. They are defined in app/models.py
==================================================================================================================		  
Q)FLASK VS DJANGO

            FLASK                                                    DJANGO
		====================                                  =========================
--Python web framework built for rapid development.	   --Python web framework built for easy and simple projects.
--Flask is WSGI framework.	                           --Django is a Full Stack Web Framework.
--Flask provides support for API.                      --Django doesn’t have any support for API.
--Flask does not offer dynamic HTML pages.	           --Django offers dynamic HTML pages.
--The request based object is imported from            --All views are set as an individual parameter in the Django.
  the flask module, which is a global 
  variable in Flask.	
--Flask is much younger platform compared to Django.	--Django is a very mature framework.
--Flask offers a diversified working style.	            --Django offers a Monolithic working style.

==================================================================================================================
Q)DJANGO MANAGE.PY

 --Manage.py in Django is a command-line utility that works similar to the django-admin command.
   The difference is that it points towards the project's settings.py file.
   This manage.py utility provides various commands that you must have while working with Django.
   
================================================================================================================
Q)SINGNALS IN DJANGO

 --Django includes a “signal dispatcher” which helps decoupled applications get notified when actions occur 
   elsewhere in the framework. 
   signals allow certain senders to notify a set of receivers 
   that some action has taken place.
   
   lie 
   pre_save
   post_save
   pre_delete
   post_delete
   request_started
   request_finished etc.,
   
   post :to create new resoruce ew can use for the first ime
   put:  to update already existing resoruce entirely
   patch: to do parital upate operations on resoruce 
   
   all these http methods we can map at calsselevel by overrding methods from super class in flask
   using resoruce class 
   we ahc ahcvie the samethign with Resoruce class in rest api calls 
   
   apis rest i ahvw owrekd 
   but fast api ddint work 
   
   but can learn quicily and wokr on it 
   no isues 
   
   no as of now 
   
   didnt work in my proejts 
   
   can learn quicly and work on it 
   
   
   c
   
   
==========================================================================================================
Q)REQUEST RESPONSE CYCLE IN DJANGO

--Thebasic principle of http protocol is the client sends a request to the server based on the request data, 
  and the server sends a response to the client. 
  We need a webserver and WSGI server while setting up the Django application 
  
===============================================================================================================
Q)ROUTERS IN DJANGO

  --Routers are used with ViewSets in django rest framework to auto config the urls.
    Routers provides a simple, quick and consistent way of wiring ViewSet logic to a set of URLs. 
    Router automatically maps the incoming request to proper viewset action based on the request 
    method type(i.e GET, POST, etc)
=======================================================================================================
Q)AUTHENTICTION IN DJANGO SESSION

 --To use session authentication, you must create a session first. 
   You must have a login resource, which accepts user credentials and authenticates a user, 
   using the Django authentication system. On requesting that resource the client will get a cookie header. 
   The cookie and csrf token must be used in future requests
 ================================================================================================
Q)DJANGO QUERYSET TO JSON FORMAT

  --Convert a QuerySet to a JSON Using a Custom Method
    Convert a QuerySet to a JSON Using Django’s Built-In Serializers
    Convert a QuerySet to a JSON Using the values() Function
	
   In Django, all the model managers return a QuerySet when some query is applied over a model. 
   A QuerySet can easily be used in Python and Django’s templating language. We can perform many actions 
   over a QuerySet to fetch the desired results or records. But a QuerySet has a drawback: 
   they are not JSON serializable.
===============================================================================================
Q)SESSION MANAGEMENT IN DJANGO

  --Django uses a cookie containing a special session id to identify each browser and 
    its associated session with the site. The actual session data is stored in the site database by default 
   (this is more secure than storing the data in a cookie, where they are more vulnerable to malicious users)
   
   tesch taskc adnd oman prejoct 
Middlewares in django
---------------------------
 In Django, middleware is a lightweight plugin that processes during request and response execution. 
 Middleware is used to perform a function in the application.  
 The middlware classes can be a security, session, csrf protection, authentication 
 
 Default middleware
 --------------------------
 Middleware is a framework of hooks into Django's request/response processing.
 It's a light, low-level “plugin” system for globally altering Django's input or output. 
 Each middleware component is responsible for doing some specific function.
 
 like csrf middleware in django 
 ----------------------------------
 The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgerie
================================================================================================================
Q)UWSGI FILE IN DJANGO uwsgi?

  --uWSGI is a fast, self-healing and developer/sysadmin-friendly application container server coded in pure C. 
    See also. The uWSGI docs offer a tutorial covering Django, nginx, and uWSGI
	
================================================================================================================	
Q)ORM IN DJANGO

  --One of the most powerful features of Django is its Object-Relational Mapper (ORM), which enables you to 
    interact with your database, like you would with SQL. In fact, Django's ORM is just 
    a pythonical way to create SQL to query and manipulate your database and get results in a pythonic fashion.
    class based views vs function based views django

jango has biltnig orm mapping suign model clases we can itnract wth db 
using orm queries ni agno views layers 

seesion
atuthenicon
message
etc.,

=================================================================================================================	
Q)MIXINS IN DJANGO

  --We started using Mixins in our Django project for HackerEarth about an year back and they truly 
    embody the DRY principle in Django. In object-oriented programming languages, 
    a mixin is a class which contains a combination of methods from other classes.
	
Q)WHAT ARE VIEW IN DJANGO

  --A view function, or “view” for short, is simply a Python function that takes a web request and returns a 
    web response. This response can be HTML contents of a web page, or a redirect, or a 404 error, or an XML 
    document, or an image, etc. 

Example:

from django.http import HttpResponse
def sample_function(request):
 return HttpResponse(“Welcome to Django”)
 
  --There are two types of views:

   Function-Based Views: In this, we import our view as a function.
   Class-based Views: It’s an object-oriented approach

django relationship with python
model manager django
django orm queries
django migrations
generic foreign key django
what ared models in django
django admin commands
different inheritance styles in django
queue objects in django
models in django
signals in django
django version  -3.0
django migrate vs makemigrations
