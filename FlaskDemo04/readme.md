# FlaskDemo04

<img src="/docs/flaskdemo04.png">

The previous example added a webpage **custqry.html** which was built by Python program **getCustData.py**. This program used an internally defined list to produce a HTML style unordered list.

In this example **getCustData.py** gets its data from a MySQL database table and generates an HTML style table.

You will need

- MySQL with the demo database SAKILA.
- pip install MYSQL connector module

From index.html the user can click a link which will

1. Run the getCustData.py
1. Generate file layouts/custqry.html (replacing if already there)
1. Display the new custqry.html in the browser


<img src="/docs/flaskdemo04-qry.png">

<hr>

1. Open a terminal or command-line window, and navigate to this folder
1. Start Flash server using the command <code>flask run</code>
1. Open a browser with URL directing to **127.0.0.1:5000** (or ip address as shown in terminal window)

## Folder Structure

- static - for style files, javascript, images, etc
- templates - for all .html files

## Programs

- app.py - default Flask application routing program
- getCustData.py - generates a HTML page from a MySQL database table

