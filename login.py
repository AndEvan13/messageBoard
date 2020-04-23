#! /usr/bin/env python3
# adapted from https://docs.python.org/3/library/http.cookies.html
from http import cookies
import mysql.connector
from mysql.connector import errorcode
import cgi
import string
import sys
import config
import hashlib, time, os, shelve


# import cgitb
# cgitb.enable()    # enable CGI traceback module

# Name: John
# UserName: TestAdmin
# Password: coolGuys21

form = cgi.FieldStorage()
val=0
username= form.getvalue('usrname') #Get username value
password= form.getvalue('pwd') #Get username value

if username!=None and password!=None:
    username=cgi.escape(username)
    password= cgi.escape(password)

    try:
        cnx = mysql.connector.connect(user=config.USER,
                                    password = config.PASSWORD,
                                    host = config.HOST,
                                    database=config.DATABASE)

    except mysql.connector.Error as err:
      #If we have an error connecting to the database we would like to output this fact.
      #This requires that we output the HTTP headers and some HTML.
      print ( "Content-type: text/html" )
      print()
      print ("""\
      <!DOCTYPE html>
      <html>
      <head>
      <meta charset = "utf-8">
      <title>DB connection with Python</title>
        <link type="text/css" rel="stylesheet" href="styles.css">
      table, td, th {border:1px solid black}
      </style>
      </head>
      <body>
      """)
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
      print("<p>Fix your code or Contact the system admin</p></body></html>")
      quit()



    cursor = cnx.cursor()

    def login(cursor,usrname,password): #class 22
        hashPass1 = hashlib.sha256(password.encode())
        hashPass = str(hashPass1.hexdigest())
        password2=hashPass
        # return 1,password2,password2
        query = "SELECT UserName, Password, Admin FROM Users WHERE UserName = (%s) AND Password = (%s);"
        data=(usrname,password2)
        try:
            cursor.execute(query,data)
          # cursor.execute(query,(usrname,))
        except mysql.connector.Error as err:
          #for DEBUG only we'll print the error and statement- we should print some generic message instead for production site
          return -1,-1,-1
        result=cursor.fetchall()
        # return -1,-1,-1
        if result!=[]:
            # return 1, result, result
            try:
                for things in result:
                    if things!=None and things!="":
                        username=things[0]
                        pwd=things[1]
                        admin=things[2]
                        # C = cookies.SimpleCookie()
                        # C["Admin"] = admin
                        # print(C)
                        return 1,username,pwd
            except:
                return -1,-1,-1
            cursor.close()
            cnx.commit()
        else:
            return -1,-1,-1


    val,user,pwd=login(cursor,username,password)
    if val==1 and username!=None and pwd!=None:
    #try to read the 'sid' cookie
        cookie = cookies.SimpleCookie()
        string_cookie = os.environ.get('HTTP_COOKIE')
        #
        if not string_cookie:
           #create the 'sid' cookie if no cookies exist
           sid = hashlib.sha256(repr(time.time()).encode()).hexdigest()
           cookie['sid'] = sid
           message = 'New session'
        else:
           #try to read the 'sid' cookie (not just any cookie)
           cookie.load(string_cookie)
           if 'sid' in cookie:
             #read the 'sid'
             sid = cookie['sid'].value
           else:
             #create new sid ans store it in a cookie
             sid = hashlib.sha256(repr(time.time()).encode()).hexdigest()
             cookie['sid'] = sid
             message = 'New session'
        cookie['sid']['expires'] = 12 * 30 * 24 * 60 * 60
        #
        # #print the cookie to tell the browser to set it
        print (cookie)

        query = "UPDATE Users SET SessionID=(%s) WHERE UserName = (%s);"
        try:
            cursor.execute(query,(sid,username))
        except mysql.connector.IntegrityError as err:
            val=-1
              # print ( "Content-type: text/html" )
              # print()
              # print ("""\
              # <!DOCTYPE html>
              # <html>
              # <head>
              # <meta charset = "utf-8">
              # <title>DB connection with Python</title>
              #   <link type="text/css" rel="stylesheet" href="styles.css">
              # table, td, th {border:1px solid black}
              # </style>
              # </head>
              # <body>
              # """)
              # if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
              #   print("Something is wrong with your user name or password")
              # elif err.errno == errorcode.ER_BAD_DB_ERROR:
              #   print("Database does not exist")
              # else:
              #   print(err)
              # print("<p>Fix your code or Contact the system admin</p></body></html>")
              # quit()
else:
    val=-1


error_msg='''Content-Type: text/html\n
<!DOCTYPE html>
<html>
<head>
<meta charset = "utf-8">
<link type="text/css" rel="stylesheet" href="styles.css">
<title>Login Check</title>
</head>
<body>
<h1>There has been an Error:</h1>
<p>please go back and try again</p>
</body></html>
'''

msg='''Content-Type: text/html\n
<!DOCTYPE html>
<html>
<head>
<meta charset = "utf-8">
<link type="text/css" rel="stylesheet" href="styles.css">
<title>Survey Feedback</title>
</head>
<body>
<h1>Welcome {user}!</h1>
<br>
<h2> You may now access the Message Board </h2>
<h3> You can click this link to get there: <a href="msgboard.py">Message Board</a></h3>
<img src="https://c8.alamy.com/comp/MBR0G5/cartoon-of-businessman-holding-big-hand-rubber-approved-stamp-MBR0G5.jpg" alt="approved">
'''

if val<1 or pwd==None:
    print (error_msg)

else:
    # code=msg.format(user=user,val=val,password=pwd) #simpler format to insert values
    code=msg.format(user=user) #simpler format to insert values
    print (code+'\n</body></html>')

cursor.close()
cnx.commit()  #this is really important otherwise all changes lost
cnx.close()
