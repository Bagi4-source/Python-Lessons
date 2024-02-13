#!/usr/bin/env python
import cgi, cgitb

from Lab6.db import Database
from Lab6.types import PlanetRequest, MoonRequest, StarRequest

db = Database()


def display_planets():
    planets = db.get_planets()
    print("<h2>Планеты</h2>")

    # Обработка данных из формы
    form = cgi.FieldStorage()
    if form.getvalue('name') and form.getvalue('radius') and form.getvalue('star_id'):
        db.add_planet(PlanetRequest(star_id=int(form.getvalue('star_id')), name=form.getvalue('name'),
                                    radius=int(form.getvalue('radius'))))
        print("<p>Планета добавлена успешно!</p>")

    print('<form action="/cgi-bin/index.py" method="post">')
    print('Название: <input type="text" name="name"><br>')
    print('Радиус (km): <input type="text" name="radius"><br>')
    print('Id звезды: <input type="text" name="star_id"><br>')
    print('<input type="submit" value="Добавить планету">')
    print('</form>')

    # Вывод данных
    print("<ul>")
    for planet in planets:
        star = db.get_star_by_id(planet.star_id)
        print(f"<li>{planet.name} - Радиус: {planet.radius} km, Звезда: {star.name}</li>")
    print("</ul>")


def display_moons():
    moons = db.get_moons()
    print("<h2>Спутники</h2>")

    # Обработка данных из формы
    moons_form = cgi.FieldStorage()
    if moons_form.getvalue('name') and moons_form.getvalue('planet_id'):
        db.add_moon(MoonRequest(planet_id=int(moons_form.getvalue('planet_id')), name=moons_form.getvalue('name')))
        print("<p>Спутник добавлен успешно!</p>")

    print('<form action="/cgi-bin/index.py" method="post">')
    print('Название: <input type="text" name="name"><br>')
    print('Id планеты: <input type="text" name="planet_id"><br>')
    print('<input type="submit" value="Добавить спутник">')
    print('</form>')

    # Вывод данных
    print("<ul>")
    for moon in moons:
        planet = db.get_planet_by_id(moon.planet_id)
        print(f"<li>{moon.name} - Спутник планеты: {planet.name}</li>")
    print("</ul>")


def display_stars():
    stars = db.get_stars()
    print("<h2>Звезды</h2>")

    # Обработка данных из формы
    stars_form = cgi.FieldStorage()
    if stars_form.getvalue('name') and stars_form.getvalue('mass'):
        db.add_star(StarRequest(mass=int(stars_form.getvalue('mass')), name=stars_form.getvalue('name')))
        print("<p>Звезда добавлена успешно!</p>")

    print('<form action="/cgi-bin/index.py" method="post">')
    print('Название: <input type="text" name="name"><br>')
    print('Масса: <input type="text" name="mass"><br>')
    print('<input type="submit" value="Добавить звезду">')
    print('</form>')

    # Вывод данных
    print("<ul>")
    for star in stars:
        print(f"<li>{star.name} - Масса: {star.mass}</li>")
    print("</ul>")


cgitb.enable()
print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print('<meta charset="utf-8">')
print("<title>Космос</title>")
print("</head>")
print("<body>")
print('<header><a href="http://localhost:8000/cgi-bin/import.py">Импорт/Экспорт</a></header>')
display_planets()
display_stars()
display_moons()
print("</body>")
print("</html>")
