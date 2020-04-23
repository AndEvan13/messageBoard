#!/usr/bin/python3
#Project 01     Created: 4/16/2020   Due: 4/22/2020  logout.py
#Created By: Celine Tannous
#Deletes Cookie

i#!/usr/bin/env python3

#session3.py
#this will delete a session if found
import hashlib, time, os, shelve
from http import cookies

import cgitb;

cgitb.enable()

cookie = cookies.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')

issession = False
sid=0
if not string_cookie:
   message = 'No cookie - no session to remove'
else:
   cookie.load(string_cookie)
   if 'sid' in cookie:
     sid = cookie['sid'].value
     issession=True
     message ="Found session - it will be deleted"
   else:
     message = 'No sid - no session to remove '
#set the variables to delete the cookie - print(cookie) will generate the correct HTTP header to set the cookie in the browser
cookie['sid'] = ''
cookie['sid']['expires'] = -1

# The shelve module will persist the session data
# and expose it as a dictionary
if issession:
  sessionFile = '/tmp/sess_' + sid
  session = shelve.open(sessionFile, writeback=True)

  #clear session data
  session.clear()
  #remove session file
  session.close()
  os.remove(sessionFile)

#produce the output, note the first parameter in the string, which is the cookie - print before the content-type line
print ("""\
%s
Content-Type: text/html\n
<html><body onload='index.html'>
<p>%s</p>
<p>SID = %s</p>
</body></html>
""" % (cookie, message, sid))
