#!/usr/bin/env python3
import datetime
import mysql.connector
from mysql.connector import errorcode
import cgi, re
import cgitb; cgitb.enable()
from config import *

form = cgi.FieldStorage()
cgitb.enable(display=0, logdir=OUTDIR)
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
  print ("""\
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

cursor = cnx.cursor()

#First we need our HTTP headers and HTML opening code
print ( "Content-type: text/html" )
print()
print ("""\
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
name = form.getvalue("name")
name = cgi.escape(name)

username = form.getvalue("usrname")
username = cgi.escape(username)

password = form.getvalue("pwd")
password = cgi.escape(password)

if (name == "") or (name == None):
    print("<p> Please enter in a name!</p>")
else:
    print("<h2> Thank you",name,"</h2>")

if (username == "") or (username == None):
    print("<p> Please enter in a UserName </p>")

if (password == "") or (password == None):
    print("<p> Please enter in a password!</p>")

print ('</body></html>')

query = ("INSERT INTO Users, (Name, UserName, Password, Admin) "
        "VALUES (" +name+","+username+","+password+","+admin+");")

cursor.execute(query)
cursor.close()
cnx.close()
