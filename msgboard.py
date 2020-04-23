#!/usr/bin/env python3
# created by MIDN Tannous & Modified by MIDN Hichue
import cgi,cgitb    #import python cgi  for traceback
from msg import msg
import config, os, hashlib, time
from http import cookies

# cgitb.enable()

import mysql.connector
from mysql.connector import errorcode

try:
    '''cnx = mysql.connector.connect(user='theuser', password = 'thepassword', host = 'thehostserver', database='thedatabase')'''
    cnx = mysql.connector.connect(user=config.USER, password = config.PASSWORD, host = config.HOST, database=config.DATABASE)


except mysql.connector.Error as err:
    print("Content-type: text/html")
    print()
    print("""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset = "utf-8">
    <title>Message Board</title>
    <style type = "text/css">
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

cookie = cookies.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')
# if 'HTTP_COOKIE' in os.environ:
#   print ("<h3>The following cookie(s) found:</h3>");
#   print (os.environ["HTTP_COOKIE"]);
sid=0
if not string_cookie:
  cookieMessage = 'No cookie - no session'
else:
    cookie.load(string_cookie)
    if 'sid' in cookie:
        sid = cookie['sid'].value

#Initiates the form
form = cgi.FieldStorage()
sendButton = form.getvalue("send")
# Queries what information to get from the database
query = "SELECT UserName, Password, Admin FROM Users WHERE SessionID = (%s);"

cursor.execute(query,(sid,))
paul=cursor.fetchall()
#Collects the data needed from the session database and loads them as variable
if paul!=[]:
    for things in paul:
        if things!=None and things!="":
            userName=things[0]
            pwd=things[1]
            admin=things[2]
# If there is no data set
else:
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
    print(error_msg)
    quit()
# If the user clicks the senndMessage button
if sendButton:

    message = form.getvalue("textarea")
    #Calls addMsg and populates the message board
    result = msg.addMsg(cursor, userName, message)

    if result == 1:
        print('Status: 303 See Other')
        print('Location: msgboard.py')
        print('Content-type: text/html')
        print()
    else:
        print("Content-Type: text/html")
        print()
        print("""\
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset = "utf-8">
        <meta http-equiv="refresh" content="5; url=msgboard.py">
        <title>Message Board</title>
        <style type = "text/css">
        table, td, th {border:1px solid black}
        </style>
        </head>
        <body>
        """)
        print('<h2>Could not send message</h2>')
        # Error statements that could occur if invalid input is inserted
        if result == 0:
            print('<p>Sorry, something unexpected happened when we tried to send your message. You will be redirected to the message board shortly.</p>')
        elif result == -1:
            print("<h3 style = 'color:red;'> User not found. Please log in.</h3><p>You will be redirected to the message board shortly.</p>")
        elif result == -2:
            print("<h3 style = 'color:red;'> Message was empty. Please enter a valid message.</h3><p>You will be redirected to the message board shortly.</p>")
        else:
            print("<p>Unexpected error code of: {: d} occurred. You will be redirected shortly.".format((result)))
        print('<p>If you are not redirected automatically, follow the <a href="msgboard.py">link to msgboard</a>. Thank you.</p>')
        print('</body></html>')

        cursor.close()
        cnx.commit()
        cnx.close()
        quit()

print("Content-type: text/html")  #Python html code that displays the html page
print()
print('''\
<!DOCTYPE html>
<html lang="en">
   <head class = "index_head">
   <meta charset="UTF-8">
     <link rel="stylesheet" href="styles.css">
      <title>Message Board</title>
   </head>
   <body>
     <nav>
   <div class="Navigation_Bar">
    <a href="index.html">Home Page</a>
    <a href="signup.html">Signup</a>
    <a href="login.html">Login</a>
    <a href="msgboard.py"> Message Board </a>
  </div>
  </nav>
 <h1>Message board</h1>
''')    #html that displays the navigation bar and the title of the message board


# if 'HTTP_COOKIE' in os.environ: #checks to see if there is a cookie present in the environment
print('''<main>
<form name='mboard' method="post" action="msgboard.py">''')
# Adds the message to the board
table = msg.printMessage(cursor)

if table:
    print(table)
else:
    print("<h2>No Messages Present</h2>")
# Adds the token identifier
token=hashlib.sha256(repr(time.time()).encode()).hexdigest()
print('''\
<p>
<label>Message:</label>
<textarea id="textarea" name="textarea" rows="4" cols="50" style="background-color: #bcf5e7;color: black;" placeholder="Message goes here..."></textarea><br>
<input type = "submit" id="send" name="send" value="Send Message">
<input type="hidden" id="token" name="token" value=token>
</p>
</form><br><br>
<a href="index.html">Log Out</a>

<footer>
    <script src="http://courses.cyber.usna.edu/SY306/docs/htmlvalidate.js"></script>
</footer>
</main>''')

cursor.close()

cnx.commit()

cnx.close()

print("</body></html>")
