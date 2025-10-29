# FlaskDemo03

<hr>

Simple website of three webpages, namely, **_Home_**, **_About_** and **_Contact_**.

In this version a new Python program is introduced, **getCustData.py**.
This folder shows how Python can generate webpages on the fly and these can be loaded by Flask.

From index.html the user can click a link which will

1. run the getCustData.py
1. generate file layouts/custqry.html (replacing if already there)
1. Flask will then display the new custqry.html in the browser

<hr>

1. Open a terminal or command-line window, and navigate to this folder
1. start Flash server using the command <code>flask run</code>
1. open a browser with URL directing to **127.0.0.1:5000** (ip address shown in terminal window)

## Folder Structure

- static - for style files, javascript, images, etc
- templates - for all .html files

## Programs

- app.py - default Flask application routing program
- getCustData.py - generates a HTML page from a list (efined inside the program)

<img src="/docs/flaskdemo03.png">
