import math


class Point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def tg(self, other: object):
        if not isinstance(other, Point):
            raise TypeError("other is not a Point")
        if other.get_x() != self.get_x():
            return (other.get_y() - self.get_y()) / (other.get_x() - self.get_x())
        return math.inf

    def dist(self, other: object) -> float:
        if not isinstance(other, Point):
            raise TypeError("other is not a Point")
        return math.sqrt((self.get_x() - other.get_x()) ** 2 + (self.get_y() - other.get_y()) ** 2)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


class Polygon(object):
    def __init__(self, points: list[Point]):
        self.points = points

    def move(self, dx, dy):
        for point in self.points:
            point.move(dx, dy)

    def square(self) -> float:
        raise Exception("Method is not overridden")

    def compare(self, o: object) -> int:
        if not isinstance(o, Polygon):
            raise TypeError("Cannot compare")

        self_square = self.square()
        other_square = o.square()

        if self_square == other_square:
            return 0
        if self_square > other_square:
            return 1
        return -1


class Triangle(Polygon):
    def __init__(self, a: Point, b: Point, c: Point):
        if not (a.dist(b) + b.dist(c) > a.dist(c) and
                a.dist(b) + a.dist(c) > b.dist(c) and
                b.dist(c) + a.dist(c) > a.dist(b)):
            raise ValueError("Invalid triangle")

        super().__init__([a, b, c])

    def square(self):
        x, y, z = self.points
        a = x.dist(y)
        b = x.dist(z)
        c = y.dist(z)
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Quad(Polygon):

    def __init__(self, a: Point, b: Point, c: Point, d: Point):
        self.dists = []
        points = [a, b, c, d]
        for i in range(4):
            for j in range(i + 1, 4):
                point1 = points[i]
                point2 = points[j]
                dist = point1.dist(point2)
                if dist:
                    self.dists.append(point1.dist(point2))
        self.dists = sorted(self.dists)
        self.base = self.dists[0]
        if not (self.dists.count(self.base) == 4 and self.dists.count(self.base * math.sqrt(2)) == 2):
            raise ValueError("Invalid quad")
        super().__init__(points)

    def square(self):
        a, b, c, d = self.points
        return a.dist(b) ** 2
