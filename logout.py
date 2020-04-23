#!/usr/bin/python3
#Project 01     Created: 4/16/2020   Due: 4/22/2020  logout.py
#Created By: Celine Tannous

import http import Cookies
import mysql.connector
import datetime
import cgi, re
import cgitb; cgitb.enable() #import python cgi for traceback
from config import *

#form = cgi.FieldStorage()
#username = form.getvalue('usrname')
#error_msg= ""
#cnx = mysql.connector.disconnect(user='m216618', database='m216618')
#cursor = cnx.cursor()

#def logout(cursor):
#    error = 0
#    query = "SELECT userName, Admin FROM USERS WHERE UserName = %s"
#    cursor.execute(query,(username))
#    try:
#        cursor.execute(query)
#    except mysql.connector.Error as err:

#Displays Page To Be The Same As The Website

#def sign_out():
    session.pop('username')
    return redirect(url_for('index'))
    # from https://gist.github.com/daGrevis/2427189
try:
  '''cnx = mysql.connector.connect(user='theuser',
                                password = 'thepassword',
                                host = 'thehostserver',
                                database='thedatabase')'''
  cnx = mysql.connector.connect(user=config.USER,
                                password = config.PASSWORD,
                                host = config.HOST,
                                database=config.DATABASE)
except mysql.connector.Error as err:
print("Content-Type: text/html\n")
print()
print('''\
<!DOCTYPE html>
<html lang="en">
<head class = "index_head">
    <link rel="shortcut icon" href="favicon.ico">
    <link type="text/css" rel="stylesheet" href="style.css">
    <title>Log Out</title>
    <meta charset="UTF-8">
   </head>
   <body>
     <nav>
   <div class="Navigation_Bar">
    <a href="index.html">Home Page</a>
    <a href="signup.html">Signup</a>
    <a href="login.html">Login</a>
    <a href="msgboard.html"> Message Board</a>
  </div>
  </nav>
  <h1 style='text-align:center;'>Log Out</h1>''')
  #html to generate log out page


  #Making This Page Look The Same As On Our Website
  print('''\
  <p style="text-align:center;"><img src="Logo2.png" width="200" alt="Logo" class="center"></p>
  ''')

print('''\

  <!--TimeStamp-->
     <footer>
        <!-- ***************************************************************
           Below this point is text you should include on every SY306 page
           *************************************************************** -->
        <script src="http://courses.cyber.usna.edu/SY306/docs/htmlvalidate.js" ></script>
  </footer>
  ''')

#if val<1:
#    code=error_msg
#    print (code+'\n<body></html>')
#else:
#    print ('\n</body></html>')

  #close cursor since we don't use it anymore
#  cursor.close()

  #commit the transaction
  cnx.commit()  #this is really important otherwise all changes lost

  #close connection
  cnx.close()

  #End html Tags
  print("</body></html>");
