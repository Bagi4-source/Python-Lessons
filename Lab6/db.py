import sqlite3
import time

from Lab6.types import *
from xml.dom.minidom import Document, parseString


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def export_to_xml(self):
        doc = Document()
        root = doc.createElement('data')
        planets_elements = doc.createElement("planets")
        stars_elements = doc.createElement("stars")
        moons_elements = doc.createElement("moons")

        for planet in self.get_planets():
            planet_element = doc.createElement("planet")

            _id = doc.createElement("id")
            _id.appendChild(doc.createTextNode(str(planet.id)))
            name = doc.createElement("name")
            name.appendChild(doc.createTextNode(planet.name))
            radius = doc.createElement("radius")
            radius.appendChild(doc.createTextNode(str(planet.radius)))
            star_id = doc.createElement("star_id")
            star_id.appendChild(doc.createTextNode(str(planet.star_id)))

            planet_element.appendChild(_id)
            planet_element.appendChild(name)
            planet_element.appendChild(radius)
            planet_element.appendChild(star_id)
            planets_elements.appendChild(planet_element)

        for moon in self.get_moons():
            moon_element = doc.createElement("moon")

            _id = doc.createElement("id")
            _id.appendChild(doc.createTextNode(str(moon.id)))
            name = doc.createElement("name")
            name.appendChild(doc.createTextNode(moon.name))
            planet_id = doc.createElement("planet_id")
            planet_id.appendChild(doc.createTextNode(str(moon.planet_id)))

            moon_element.appendChild(_id)
            moon_element.appendChild(name)
            moon_element.appendChild(planet_id)
            moons_elements.appendChild(moon_element)

        for star in self.get_stars():
            star_element = doc.createElement("star")

            _id = doc.createElement("id")
            _id.appendChild(doc.createTextNode(str(star.id)))
            name = doc.createElement("name")
            name.appendChild(doc.createTextNode(star.name))
            mass = doc.createElement("mass")
            mass.appendChild(doc.createTextNode(str(star.mass)))

            star_element.appendChild(_id)
            star_element.appendChild(name)
            star_element.appendChild(mass)
            stars_elements.appendChild(star_element)

        root.appendChild(planets_elements)
        root.appendChild(stars_elements)
        root.appendChild(moons_elements)
        doc.appendChild(root)
        name = f"temp/export_{int(time.time())}.xml"
        with open(name, "w") as f:
            f.write(doc.toprettyxml())
        return name

    def import_xml(self, binary):
        dom = parseString(binary)
        planets = dom.getElementsByTagName("planet")
        moons = dom.getElementsByTagName("moon")
        stars = dom.getElementsByTagName("star")
        for planet in planets:
            planet_id = int(planet.getElementsByTagName("id")[0].firstChild.nodeValue)
            planet_name = planet.getElementsByTagName("name")[0].firstChild.nodeValue
            planet_radius = float(planet.getElementsByTagName("radius")[0].firstChild.nodeValue)
            planet_star_id = int(planet.getElementsByTagName("star_id")[0].firstChild.nodeValue)
            self.save_planet(Planet(id=planet_id, name=planet_name, radius=planet_radius, star_id=planet_star_id))

        for moon in moons:
            moon_id = int(moon.getElementsByTagName("id")[0].firstChild.nodeValue)
            moon_name = moon.getElementsByTagName("name")[0].firstChild.nodeValue
            moon_planet_id = int(moon.getElementsByTagName("planet_id")[0].firstChild.nodeValue)
            self.save_moon(Moon(id=moon_id, name=moon_name, planet_id=moon_planet_id))

        for star in stars:
            star_id = int(star.getElementsByTagName("id")[0].firstChild.nodeValue)
            star_name = star.getElementsByTagName("name")[0].firstChild.nodeValue
            star_mass = float(star.getElementsByTagName("mass")[0].firstChild.nodeValue)
            self.save_star(Star(id=star_id, name=star_name, mass=star_mass))

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS planets (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            radius REAL,
                            star_id INTEGER,
                            FOREIGN KEY (star_id) REFERENCES stars(id)
                        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS stars (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            mass REAL
                        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS moons (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            planet_id INTEGER,
                            FOREIGN KEY (planet_id) REFERENCES planets(id)
                        )''')

        self.cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS planets_id ON planets(id);')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS planets_star_id ON planets(star_id);')
        self.cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS stars_id ON stars(id);')
        self.cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS moons_id ON moons(id);')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS moons_planet_id ON moons(planet_id);')

        self.connection.commit()

    def save_planet(self, planet: Planet):
        self.cursor.execute('''INSERT INTO planets (id, name, radius, star_id) VALUES (?, ?, ?, ?)
         ON CONFLICT(id) DO UPDATE SET name = ?, radius = ?, star_id = ?''', (
            planet.id, planet.name, planet.radius, planet.star_id, planet.name, planet.radius, planet.star_id))
        self.connection.commit()

    def save_moon(self, moon: Moon):
        self.cursor.execute('''INSERT INTO moons (id, name, planet_id) VALUES (?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET name = ?, planet_id = ?''', (
            moon.id, moon.name, moon.planet_id, moon.name, moon.planet_id))
        self.connection.commit()

    def save_star(self, star: Star):
        self.cursor.execute('''INSERT INTO stars (id, name, mass) VALUES (?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET name = ?, mass = ?''', (
            star.id, star.name, star.mass, star.name, star.mass))
        self.connection.commit()

    def add_star(self, star: StarRequest):
        self.cursor.execute('INSERT INTO stars (name, mass) VALUES (?, ?)', (star.name, star.id))
        self.connection.commit()

    def add_planet(self, planet: PlanetRequest):
        self.cursor.execute('INSERT INTO planets (name, radius, star_id) VALUES (?, ?, ?)',
                            (planet.name, planet.radius, planet.star_id))
        self.connection.commit()

    def add_moon(self, moon: MoonRequest):
        self.cursor.execute('INSERT INTO moons (name, planet_id) VALUES (?, ?)',
                            (moon.name, moon.planet_id))
        self.connection.commit()

    def get_planets(self) -> list[Planet]:
        planets = self.cursor.execute("SELECT * FROM planets").fetchall()
        return list(map(Planet.mapper, planets))

    def get_planet_by_id(self, id: int) -> Planet:
        planet = self.cursor.execute("SELECT * FROM planets WHERE id=?", (id,)).fetchone()
        return Planet.mapper(planet)

    def get_moons(self) -> list[Moon]:
        moons = self.cursor.execute("SELECT * FROM moons").fetchall()
        return list(map(Moon.mapper, moons))

    def get_moon_by_id(self, id: int) -> Moon:
        moon = self.cursor.execute("SELECT * FROM moons WHERE id=?", (id,)).fetchone()
        return Moon.mapper(moon)

    def get_moons_by_planet_id(self, planet_id: int) -> list[Moon]:
        moons = self.cursor.execute("SELECT * FROM moons WHERE planet_id=?", (planet_id,)).fetchall()
        return list(map(Moon.mapper, moons))

    def get_star_by_id(self, id: int) -> Star:
        star = self.cursor.execute("SELECT * FROM stars WHERE id=?", (id,)).fetchone()
        return Star.mapper(star)

    def get_stars(self) -> list[Star]:
        stars = self.cursor.execute("SELECT * FROM stars").fetchall()
        return list(map(Star.mapper, stars))

    def close(self):
        self.connection.commit()
        self.connection.close()
