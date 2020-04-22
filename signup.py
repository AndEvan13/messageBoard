#!/usr/bin/env python3
#Everything we need to connnect to the database
import mysql.connector
from mysql.connector import errorcode
#What we need to read the forms
import cgi, re
import cgitb; cgitb.enable()
import config
#For hashing the passwords
import hashlib

form = cgi.FieldStorage()

#Connect to the database
try:
  '''cnx = mysql.connector.connect(user='theuser',
                                password = 'thepassword',
                                host = 'thehostserver',
                                database='thedatabase')'''
  cnx = mysql.connector.connect(user=config.USER,
                                password = config.PASSWORD,
                                host = config.HOST,
                                database=config.DATABASE)

#check for errors
except mysql.connector.Error as err:
  #If we have an error connecting to the database we would like to output this fact.
  #This requires that we output the HTTP headers and some HTML.
  print ( "Content-type: text/html" )
  print()
  print ("""
  <!DOCTYPE html>
  <html>
  <head>
  <meta charset = "utf-8">
  <title>DataBase not connected</title>
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
#Connects to database
cursor = cnx.cursor()

#First we need our HTTP headers and HTML opening code
print ( "Content-type: text/html" )
print()
print ("""
<!DOCTYPE html>
<html>
<head>
<meta charset = "utf-8">
<title>Sign-up Results</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
""")
#create the page
print ("<h1>Sign-up Results</h1>")

#This gets all of the values for the Form
#Presents XSS attacks
nameOrig = form.getvalue("name")
name = cgi.escape(nameOrig)

usernameOrig = form.getvalue("usrname")
username = cgi.escape(usernameOrig)

passwordOrig = form.getvalue("pwd")
password = cgi.escape(passwordOrig)

password2Orig = form.getvalue("pwd2")
password2 = cgi.escape(password2Orig)

admin = "0"

#Re-error checking
x = 0

pas = str(password)
passCheck1 = re.search(r'w{6,}[0-9]{1,}', pas)
passCheck2 = bool(passCheck1)

if (name == "") or (name == None):
    print("<p> Please enter in a name!</p>")
    x = 1

if (username == "") or (username == None):
    print("<p> Please enter in a UserName </p>")
    x = 1

# if passCheck2 != True:
#     print("<p> Please follow the correct password format.</p>")
#     x = 1

if (password == "") or (password == None):
    print("<p> Please enter in a password!</p>")
    x = 1

if (password != password2):
    print("<p> Passwords do not match!</p>")
    x = 1


#Hashing the password
hashPass1 = hashlib.sha256(password.encode())
hashPass = str(hashPass1)
#Prevents SQL injections
query = "Insert into Users Values (%s,%s,%s,%s)"
try:
    cursor.execute(query,(name,username,hashPass,admin))
except mysql.connector.IntegrityError as err:
    print("<h1> Sorry that username is already taken! Please try another!")
    print("<a href='http://midn.cyber.usna.edu/~m212748/Project1/signup.html'>")
    print("<br> Sign-Up! </a>")
    x = 1

if (x == 0):
    print("<h1> Thank you",name,"for signing up for Let's talk about it!<br><br>")
    print("<h1> Please click the link below to log-in and begin messaging!")
    print("<a href='http://midn.cyber.usna.edu/~m212748/Project1/login.html'>")
    print("<br> Log-In!</a>")

print ('</body></html>')
cursor.close()
cnx.commit()
cnx.close()