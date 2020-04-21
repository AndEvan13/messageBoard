 #!/usr/bin/env python3

import cgi,cgitb    #import python cgi  for traceback
from msg import msg

cgitb.enable()

import mysql.connector
from mysql.connnector import errorcode

import config


try:
    '''cnx = mysql.connector.connect(user='theuser', password = 'thepassword', host = 'thehostserver', database='thedatabase')'''
    cnx = mysql.connector.connect(user=config.USER, password = config.PASSWORD, host = config.HOST, database=config.DATABASE)


except mysql.connector.Error as err:
    print("Content-type: text/html")
    print()
    print("""\
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
elif err.errno == errocode.ER_BAD_DB_ERROR:
    print("Database does not exist")
else:
    print(err)
print("<p>Fix your code or Contact the system admin</p></body></html>")
quit()

cursor = cnx.cursor()

params = cgi.FieldStorage()
insertButton = params.getvalue("insert")

if insertButton:
    #need to insert code right how that stores the userName of the person accessing the messageboard as a variable
    message = params.getvalue("message")

    result = msg.addMsg(cursor, user, message)

    if result == 1:
        print('Status: 303 See Other')
        print('Location: msgboard.py')
        print('Content-type: text/html')
        print()
    else:
        print('Content-type: text/html')
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

        if result == 0:
            print('<p>Sorry, something unexpected happened when we tried to send your message. You will be redirected to the message board shortly.</p>')
        elif result == -1:
            print("<h3 style = 'color:red'> User not found. Please log in.</h3><p>You will be redirected to the message board shortly.</p>")
        elif result == -2:
            print("<h3 style = 'color:red'> Message was empty. Please enter a valid message.</h3><p>You will be redirected to the message board shortly.</p>")
        else:
            print("<p>Unexpected error code of: {: d} occurred. You will be redirected shortly.".format((result)))
        print('<p>If you are not redirected automatically, follow the <a href="msgboard.py">link to msgboard</a>. Thank you.</p>')
        print('</body></html>')

        cursor.close()
        cnx.commit()
        cnx.close()
        quit()


print("Content-Type: text/html\n")  #Python html code that displays the html page
print('''\
<!DOCTYPE html>
<html lang="en">
   <head class = "index_head">
     <link rel="stylesheet" href="styles.css">
      <title>Message Board</title>
      <meta charset="UTF-8">
   </head>
   <body>
     <nav>
   <div class="Navigation_Bar">
    <a href="signup.html">Signup</a>
    <a href="login.html">Login</a>
    <a href="msgboard.html"> Message Board </a>
  </div>
  </nav>
 <h1>Message board</h1>
''')    #html that displays the navigation bar and the title of the message board


if 'HTTP_COOKIE' in os.environ: #checks to see if there is a cookie present in the environment
    print('''<main>
    <form method="post" action="msgboard.py">''')

    table = msg.printMessage(cursor)

    if table:
        print(table)
    else:
        print("<h2>No Messages Present</h2>")


    print('''<table id="msgboard"><tbody><tr><th>Username</th><th>Message</th></tr>
    </tbody></table>
    <p>
    <label>Message: <input type="textbox" name="message"></label><br>
    <input type="submit" name="insert" value="Send Message">
    </p>
    </form><br><br>
    <a href="logout.py">Log Out</a>

    <footer>
        <script src="http://courses.cyber.usna.edu/SY306/docs/htmlvalidate.js"></script>
    </footer>
    </main>''')

    cursor.close()

    cnx.commit()

    cnx.close()

    print('''
        </body>
    </html>
    ''')   #displays the msgboard if the user's cookie has been verified

else:   # if the user's cookie has not been verified display an error message instead of the msg board
    print("<h3> You must be logged in first to access this page. Please try again.</h3></body></html>")
    exit(0)
