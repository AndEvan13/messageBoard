#!/usr/bin/env python3
import datetime
import mysql.connector
import cgi, re
import cgitb; cgitb.enable()
import config

form = cgi.FieldStorage()

cnx = mysql.connector.connect(user=config.USER,
                            password = config.PASSWORD,
                            host = config.HOST,
                            database=config.DATABASE)
cursor = cnx.cursor()

print ("Content-Type: text/html")
print ()
print ('''
<!DOCTYPE html>
<html>
<head>
<meta charset = "utf-8">
<title>Signup Feedback</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
''')

#This gets all of the values for the Form
name = form.getvalue("name")
username = form.getvalue("usrname")
password = form.getvalue("pwd")

if (name == "") or (name == None):
    print("<p> Please enter in a name!</p>")
else:
    print("<h2> Thank you",name,"</h2>")

if (username == "") or (username == None):
    print("<p> Please enter in a UserName </p>")

if (password == "") or (password == None):
    print("<p> Please enter in a password!</p>")

print ('</body></html>')

query = ("INSERT INTO USERS, (Name, UserName, Password, Admin) "
        "VALUES (" +name+","+username+","+password+","+admin+");")

cursor.execute(query)
cursor.close()
cnx.close()
