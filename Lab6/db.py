import sqlite3
from pydantic import BaseModel


class Star(BaseModel):
    id: int
    name: str
    mass: float


class Planet(BaseModel):
    id: int
    name: str
    radius: float
    star_id: int


class Moon(BaseModel):
    id: int
    name: str
    planet_id: int


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        self.create_table()

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
                            mass REAL,
                        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS moons (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            planet_id INTEGER,
                            FOREIGN KEY (planet_id) REFERENCES planets(id),
                        )''')

    def add_star(self, star: Star):
        self.cursor.execute('INSERT INTO stars (name, mass) VALUES (?, ?)', (star.name, star.id))

    def add_planet(self, planet: Planet):
        self.cursor.execute('INSERT INTO planet (name, radius, star_id) VALUES (?, ?, ?)',
                            (planet.name, planet.radius, planet.star_id))

    def add_moon(self, moon: Moon):
        self.cursor.execute('INSERT INTO planet (name, planet_id) VALUES (?, ?)',
                            (moon.name, moon.planet_id))

    def close(self):
        self.connection.commit()
        self.connection.close()
