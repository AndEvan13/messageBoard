#!/usr/bin/python3

import cgitb    #import python cgi modulo for traceback errors
cgitb.enable()

print("Content-Type: text/html\n")  #Python html code that displays the html page
print('''\
<!DOCTYPE html>
<html lang="en">
   <head class = "index_head">
     <link rel="stylesheet" href="styles.css">
      <title>Epstein Didn't Kill Himself</title>
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
''')

if 'HTTP_COOKIE' in os.environ: #checks to see if there is a cookie present in the environment
    print('''<main>
    <form method="post" action="msgboard.py">
    <table id="msgboard"><tbody><tr><th>Username</th><th>Message</th></tr>
    </tbody></table>
    <p>
    <label>Message: <input type="textbox" name="message"></label><br>
    <input type="submit" name="insert" value="Send Message">
    </p>
    </form><br><br>
    <a href="logout.py">Log Out</a>
    ''')    #displays the msgboard if the user's cookie has been verified

else:   # if the user's cookie has not been verified display an error message instead of the msg board
    print("<h3> You must be logged in first to access this page. Please try again.</h3></body></html>")
    exit(0)
