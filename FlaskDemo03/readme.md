# FlaskDemo03

In this version a new Python program is introduced, **getCustData.py**.

<img src="/docs/flaskdemo03.png">

This folder shows how Python can generate HTML webpages on the fly and these can be loaded by Flask.

**index.html** has a link which when clicked...

1. Runs getCustData.py
1. Generates **layouts/custqry.html** (replacing if already there)
1. Uses Flask to display the new custqry.html

<hr>

1. Open a terminal or command-line window, and navigate to this folder
1. Start Flash server using the command <code>flask run</code>
1. Open a browser with URL directing to **127.0.0.1:5000** (or ip address as shown in terminal window)

## Folder Structure

- static - for style files, javascript, images, etc
- templates - for all .html files

## Programs

- app.py - default Flask application routing program
- getCustData.py - generates a HTML page from a list (defined inside the program)
