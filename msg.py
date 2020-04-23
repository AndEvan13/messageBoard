#!/usr/bin/python3

import mysql.connector

class msg:
    def __init__(self):
        pass

    def addMsg(cursor, user, Message):
        #Sanity checks of the Message
        if Message == None:
            print('Content-type: text/html')
            print()
            print('<!DOCTYPE html><html><head><meta charset="utf-8"><title>SQL Error</title></head>')
            print('<body>')
            print("<h3>Message field was not filled. Please enter a valid Message.</h3>")
            print('</body></html>')


        if user == None:
            return -1
        if Message == None:
            return -2

        query = "Insert into Messages(userName, Message) values ('" + user +"','" + Message + "')"

        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print('Content-type: text/html')
            print()
            print('<!DOCTYPE html><html><head><meta charset="utf-8"><title>SQL Error</title></head>')
            print('<body>')
            print('<p style = "color:red;">')
            print(err)
            print('</p>')
            print('</body></html>')

        nbRowsInserted = cursor.rowcount
        MessageID = cursor.lastrowid

        if nbRowsInserted > 0:

            return 1
        else:
            return 0


    def printMessage(cursor):
        query = "SELECT MessageID, userName, Message FROM Messages"
        try:
            cursor.execute(query)
        except mysql.connector.Error as err:
            print('<p style = "color:red">')
            print(err)
            print(" for statement" + cursor.statement )
            print('</p>')

        nbRows = 0

        table = "<table><tr><th>MessageID</th><th>User</th><th>Message</th></tr>\n"
        for (MessageID, user, Message) in cursor:
            table += "<tr><td>" + str(MessageID) + "</td><td>" + user + "</td><td>" + Message + "</td></tr>\n"
            nbRows += 1
        table += "</table>"

        if nbRows > 0:
            return table
        else:
            return ""
