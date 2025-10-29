
myData = [ "Jack", "Jill", "Fred", "Wilma", "Barney", "Betty"]



htmlString = '{% extends "layout.html" %}\n'
htmlString += '{% block heading %}<h1>Customery Query</h1>{% endblock %}\n'


# create HTML unordered list
htmlString+= '{% block main %}\n'

htmlString += "<ul>"
# loop through the Python list
for name in myData:
    htmlString += f"<li>{name}</li>\n"

# close the <UL> tag
htmlString+= "</ul>"

htmlString+= '{% endblock %}\n'




# write HTML string to text file
myFile = open("templates/custqry.html" , "wt" )
myFile.write(htmlString)
myFile.close()