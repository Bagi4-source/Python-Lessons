from pydantic import BaseModel


class StarRequest(BaseModel):
    name: str
    mass: float


class Star(StarRequest):
    id: int

    @staticmethod
    def mapper(star: tuple):
        return Star(id=star[0], name=star[1], mass=star[2])


class PlanetRequest(BaseModel):
    name: str
    radius: float
    star_id: int


class Planet(PlanetRequest):
    id: int

    @staticmethod
    def mapper(planet: tuple):
        return Planet(id=planet[0], name=planet[1], radius=planet[2], star_id=planet[3])


class MoonRequest(BaseModel):
    name: str
    planet_id: int


class Moon(MoonRequest):
    id: int

    @staticmethod
    def mapper(moon: tuple):
        return Moon(id=moon[0], name=moon[1], planet_id=moon[2])
