#! /usr/bin/env python3
# adapted from https://docs.python.org/3/library/http.cookies.html
from http import cookies
import mysql.connector
import cgitb      # import CGI traceback module

cgitb.enable()    # enable CGI traceback module

form = cgi.FieldStorage()
username= form.getvalue('usrname') #Get username value
error_msg=""
cnx = mysql.connector.connect(user='m216618', database='m216618')
cursor = cnx.cursor()

def login(cursor):
    error = 0
    query = "SELECT UserName, Admin FROM USERS WHERE UserName = %s"
    cursor.execute(query,(username))
    try:
      cursor.execute(query)
    except mysql.connector.Error as err:
      #for DEBUG only we'll print the error and statement- we should print some generic message instead for production site
      return -1

    for (username, admin) in cursor:
        cookie = cookies.SimpleCookie()
        cookie[username]=admin
        print(cookie)
    return 1


val=login(cursor)

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
<h1>Welcome {username}!</h1>
<br>
<p> You may now access the Message Board </p>
'''

if val<1:
    code=error_msg
    print (code+'\n</body></html>')

else:
    code=msg.format(username=username) #simpler format to insert values
    # print("<p>")
    # print(os.environ["HTTP_COOKIE"])
    # print("</p>")
    print (code+'\n</body></html>')
#close cursor since we don't use it anymore
cursor.close()

#commit the transaction
cnx.commit()  #this is really important otherwise all changes lost

#close connection
cnx.close()

