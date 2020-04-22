#!/usr/bin/python3

import cgitb #import python cgi for traceback
cgitb.enable()

print("Content-Type: text/html\n")
print('''\
<!DOCTYPE html>
<html lang="en">
   <head class = "index_head">
     <link rel="stylesheet" href="styles.css">
      <title>Log Out</title>
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
  <h1>Log Out</h1>''') #html to generate log out page
