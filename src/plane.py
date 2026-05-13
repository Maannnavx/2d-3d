from src.point import Point3D
from src.vector import Vector3D

class Plane:
    def __init__(self, point: Point3D, normal: Vector3D):
        self.point = point
        self.normal = normal

    @classmethod
    def from_three_points(cls, p1: Point3D, p2: Point3D, p3: Point3D):
        v1 = Vector3D(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)
        v2 = Vector3D(p3.x - p1.x, p3.y - p1.y, p3.z - p1.z)
        normal = v1.cross(v2)
        return cls(p1, normal)

    def __repr__(self):
        return f"Plane(point={self.point}, normal={self.normal})"
    
    def contains_point(self, p: Point3D):
        v = Vector3D(p.x - self.point.x, p.y - self.point.y, p.z - self.point.z)
        return round(self.normal.dot(v), 10) == 0

    def distance_to_point(self, p: Point3D):
        v = Vector3D(p.x - self.point.x, p.y - self.point.y, p.z - self.point.z)
        return abs(self.normal.dot(v)) / self.normal.magnitude()

    def is_parallel(self, other):
        cross = self.normal.cross(other.normal)
        return all(round(c, 10) == 0 for c in cross.components)

    def is_perpendicular(self, other):
        return round(self.normal.dot(other.normal), 10) == 0