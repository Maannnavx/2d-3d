import math

class Point:
    def __init__(self, *coords):
        self.coords = coords

    def distance_to(self, other):
        return math.sqrt(sum((a - b)**2 for a, b in zip(self.coords, other.coords)))

    def __repr__(self):
        return f"Point{len(self.coords)}D{self.coords}"


class Point2D(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y


class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z