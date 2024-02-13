#!/usr/bin/env python
import cgi, cgitb

from Lab6.db import Database

db = Database()


def add_form():
    form = cgi.FieldStorage()
    if form.getvalue('filename'):
        db.import_xml(form.getvalue('filename'))

    print("""
    <form enctype = "multipart/form-data" action = "import.py" method = "post">
    <p>Файл: <input type = "file" name = "filename" /></p>
    <p><input type = "submit" value = "Импорт" /></p>
    </form>
    """)


cgitb.enable()
print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print('<meta charset="utf-8">')
print("<title>Космос</title>")
print("</head>")
print("<body>")
print('<header><a href="http://localhost:8000/cgi-bin/index.py">Главная</a></header>')
print("<h2>Экспорт</h2>")
add_form()
print("""
<form action = "export.py" method = "get">
<p><input type = "submit" value = "Экспорт" /></p>
</form>
""")
print("</body>")
print("</html>")
