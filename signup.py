import mysql.connector
# Creation of a Users class to record who our member database

class Users:
  # This class is used to add users to the database

  def __init__(self):
    pass

  #songID is AUTO_INCREMENT and votes has a default of 0, so no need to worry about them
  def addUser(cursor, name, username, password):
    #Before we create the query statement a sanity check of the passed values should be run.
    ##  print ("<h3 style = 'color:red'> Artist or Title was empty. Please enter a valid value.</h3>")
    ##  return False
    if username == None and password == None:
      ##print ("<h3 style = 'color:red'> Artist or Title was empty. Please enter a valid value.</h3>")
      return -3
    if artist == None:
      return -1
    if title == None:
      return -2
    #create query statement
    query = "INSERT INTO USERS(name, username, password, admin) values ('" + artist + "','" + title + "')"
    #execute the query
    try:
      cursor.execute(query)
    except mysql.connector.Error as err:
      #for DEBUG only we'll print the error - we should print some generic message instead for production site

      #If we are going to debug, we need to declare the HTTP Headers and html then exit
      print ('Content-type: text/html')
      print()
      print ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>SQL Error</title></head>')
      print ('<body>')
      print ('<p style = "color:red">')
      print (err)
      print ('</p>')
      #close the document
      print ('</body></html>')

    #check number of rows affected > 0 if insert successful
    nbRowsInserted = cursor.rowcount
    songID = cursor.lastrowid #get the last songid inserted

    if nbRowsInserted > 0:

      ##return songID
      return 1
    else:
      ##return False
      return 0


  def printSongs(cursor):
    query = "SELECT SongID, Artist, Title, Votes FROM songs ORDER BY Artist, Title"
    # query = "SELECT Artist FROM songs ORDER BY Artist, Title"  # if only one column returned, make sure we read it as a tuple of 1 element, which is (col1,)
    try:
      cursor.execute(query)
    except mysql.connector.Error as err:
      #for DEBUG only we'll print the error and statement- we should print some generic message instead for production site
      print ('<p style = "color:red">')
      print(err)
      print (" for statement" + cursor.statement )
      print ('</p>')

    nbRows = 0
    #create a table with results
    table = "<table><tr><th>SongID</th><th>Artist</th><th>Title</th><th>Votes</th></tr>\n"
    for (songID, artist, title, votes) in cursor:
    # for (artist,) in cursor: #do something like this if only one column, artist in the example, is returned - needs to be a tuple, so have the ,
       table += "<tr><td>"+str(songID) + "</td><td>" + artist+"</td><td>"+title+"</td><td>" + str(votes) + "</td></tr>\n"
       nbRows+=1
    table += "</table>"

    if nbRows > 0:
      return table
    else:
      return ""