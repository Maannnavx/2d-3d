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

    def intersection(self, other):
        d1 = self.direction.components
        d2 = other.direction.components
        p1 = self.point.coords
        p2 = other.point.coords

        cross = d1[0] * d2[1] - d1[1] * d2[0]
        if round(cross, 10) == 0:
            return None  # lines are parallel, no intersection

        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        t = (dx * d2[1] - dy * d2[0]) / cross
        return self.point_at(t)
    
    def closest_points(self, other):
        d1 = self.direction.components
        d2 = other.direction.components
        p1 = self.point.coords
        p2 = other.point.coords

        w = tuple(p1[i] - p2[i] for i in range(len(p1)))
        a = sum(a * b for a, b in zip(d1, d1))
        b = sum(a * b for a, b in zip(d1, d2))
        c = sum(a * b for a, b in zip(d2, d2))
        d = sum(a * b for a, b in zip(d1, w))
        e = sum(a * b for a, b in zip(d2, w))

        denom = a * c - b * b
        if round(denom, 10) == 0:
            return None  # lines are parallel

        t1 = (b * e - c * d) / denom
        t2 = (a * e - b * d) / denom
        return self.point_at(t1), other.point_at(t2)

class Line2D(Line):
    def __init__(self, point: Point2D, direction: Vector2D):
        super().__init__(point, direction)


class Line3D(Line):
    def __init__(self, point: Point3D, direction: Vector3D):
        super().__init__(point, direction)

