from src.point import Point, Point2D, Point3D
from src.vector import Vector, Vector2D, Vector3D

class Line:
    def __init__(self, point, direction):
        self.point = point
        self.direction = direction

    def __repr__(self):
        return f"Line(point={self.point}, direction={self.direction})"
    
    def point_at(self, t):
        new_coords = tuple(p + t * d for p, d in zip(self.point.coords, self.direction.components))
        return Point(*new_coords)
    
    def contains_point(self, p):
        diffs = [p.coords[i] - self.point.coords[i] for i in range(len(p.coords))]
        ratios = set()
        for diff, d in zip(diffs, self.direction.components):
            if d != 0:
                ratios.add(round(diff / d, 10))
        return len(ratios) == 1
    
    def distance_to_point(self, p):
        ap = tuple(p.coords[i] - self.point.coords[i] for i in range(len(p.coords)))
        ap_vec = Vector(*ap)
        t = ap_vec.dot(self.direction) / self.direction.dot(self.direction)
        closest = self.point_at(t)
        return p.distance_to(closest)

    def is_parallel(self, other):
        d1 = self.direction.components
        d2 = other.direction.components
        cross = [a * b2 - a2 * b for a, a2, b, b2 in zip(d1, d1[1:], d2, d2[1:])]
        return all(round(c, 10) == 0 for c in cross)

    def is_perpendicular(self, other):
        return self.direction.dot(other.direction) == 0


class Line2D(Line):
    def __init__(self, point: Point2D, direction: Vector2D):
        super().__init__(point, direction)


class Line3D(Line):
    def __init__(self, point: Point3D, direction: Vector3D):
        super().__init__(point, direction)

