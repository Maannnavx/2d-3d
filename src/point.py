import math

class Point:
    def __init__(self, *coords):
        self.coords = coords

    def distance_to(self, other):
        return math.sqrt(sum((a - b)**2 for a, b in zip(self.coords, other.coords)))

    def midpoint(self, other):
        mid_coords = tuple((a + b) / 2 for a, b in zip(self.coords, other.coords))
        return Point(*mid_coords)

    def __repr__(self):
        return f"Point{len(self.coords)}D{self.coords}"
    
    def __eq__(self, other):
        return self.coords == other.coords
    
    def __len__(self):
        return len(self.coords)
    
    def __iter__(self):
        return iter(self.coords)
    
    def distance_to_origin(self):
        origin = Point(*[0] * len(self.coords))
        return self.distance_to(origin)


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