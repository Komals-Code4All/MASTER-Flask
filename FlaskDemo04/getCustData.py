'''   
    Fetch data from a MySQL database table and display it as an HTML table

'''

# mysql connection module
import mysql.connector

qryData = []  # list to hold data returned by SQL query

def getSQLData():
    ''' Conect to SQL datbase and run the SELECT query '''

    global qryData
    qryString = "SELECT first_name,last_name,email FROM customer ORDER BY last_name LIMIT 20"

    # connect to SAKILA database
    mydb = mysql.connector.connect(host='localhost', user='root', password='sqluser', database='sakila'   )
    mycursor = mydb.cursor()        # create a 'pointer' object
    mycursor.execute(qryString)     # run the SELECT query
    qryData = mycursor.fetchall()   # store the returned data in a list
    

def buildHTML():
    ''' Build a web page from the data returned by the SQL query '''

    # insert Flask code to make use of a default layout template
    htmlString = '{% extends "layout.html" %}\n'
    htmlString += '{% block heading %}<h1>Customery Query</h1>{% endblock %}\n'

    # start with a Flask template 'block'
    htmlString+= '{% block main %}\n'

    # create HTML table
    htmlString += "<table>"
    htmlString += f"<thead><tr><th>Last Name</th><th>First Name</th><th>Email</th></tr><thead><tbody>\n"

    # loop through the data returned by SQL query
    for data in qryData:
        fname=data[0].capitalize()  # firstname
        lname=data[1].capitalize()  # last name
        email=data[2].lower()       # email address

        # HTML table row
        htmlString += f"<tr><td>{lname}</td><td>{fname}</td><td>{email}</td></tr>\n"

    # close the table tag
    htmlString+= f"</tbody><tfoot><tr><td colspan='3'>{len(qryData)} records displayed</td></tr></tfoot></table>"
 

    # close the Flask template 'block'
    htmlString+= '{% endblock %}\n'


    # Finally, create custqry.html file in Flask's templates folder
    myFile = open("templates/custqry.html" , "wt" )  # open for Writing, Text
    myFile.write(htmlString)
    myFile.close()

#--------------------------------------------
# Main Processing
#--------------------------------------------

getSQLData()        # fetch data from SQL table
buildHTML()         # build and create the custqry.html file
