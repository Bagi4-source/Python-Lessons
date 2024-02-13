#!/usr/bin/env python
import cgi, cgitb

from Lab6.db import Database

db = Database()

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
print(f'<a href="../{db.export_to_xml()}">Файл</a>')
print("</body>")
print("</html>")
