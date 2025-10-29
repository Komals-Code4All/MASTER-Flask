# FlaskDemo02

Simple website of three webpages, namely, **_Home_**, **_About_** and **_Contact_**.

You will have noticed that the three webpages have very similar html coding. For example they have the same opening header, navigation and footer html. 

Flask allows a special template file that can be used to define a standard layout for all webpages. This file is named **layout.html** and can be found in the **templates** folder with all the other HTML files.

Within the layout.html file there are empty spaces, or **blocks** where other webpages will inseret their particualr HTML code.  


A block is defined using the **jinja** syntax. The block definition must left empty in **layout.html** file.

<code>
    {% block    block-name %}

    {% endblock %}
</code>

A jinja command <code>{% extends "layout.html" %}</code> at the top of the HTML file instructs Flask to use the layout.html template.

Then HTML tags defined inside a block will be inserted into the corresponding empty block (on the template.html).

<code>
    {% block    block-name %}
        <h2>Welcome to my web page</h2>
        <p>Lorem ipsum dolor, sit amet consectetur</p>
    {% endblock %}
</code>




1. Open a terminal or command-line window, and navigate to this folder
1. start Flash server using the command <code>flask run</code>
1. open a browser with URL directing to **127.0.0.1:5000** (ip address shown in terminal window)

## Folder Structure

- static - for style files, javascript, images, etc
- templates - for all .html files

## Programs

- app.py - default Flask application routing program

<img src="/docs/flaskdemo01.png">
