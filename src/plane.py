from src.point import Point3D
from src.vector import Vector3D
from src.line import Line3D

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
    
    def intersection_with_line(self, line):
        d = self.normal.dot(Vector3D(*line.direction.components))
        if round(d, 10) == 0:
            return None  # line is parallel to plane

        v = Vector3D(
            line.point.x - self.point.x,
            line.point.y - self.point.y,
            line.point.z - self.point.z
        )
        t = -self.normal.dot(v) / d
        return line.point_at(t)
    
    def intersection_with_plane(self, other):
        direction = self.normal.cross(other.normal)
        if all(round(c, 10) == 0 for c in direction.components):
            return None  # planes are parallel

        n1 = self.normal.components
        n2 = other.normal.components
        d1 = sum(n1[i] * self.point.coords[i] for i in range(3))
        d2 = sum(n2[i] * other.point.coords[i] for i in range(3))

        # try XY plane first
        denom = n1[0]*n2[1] - n1[1]*n2[0]
        if round(denom, 10) != 0:
            x = (d1*n2[1] - d2*n1[1]) / denom
            y = (d2*n1[0] - d1*n2[0]) / denom
            point = Point3D(x, y, 0)
        else:
            # try YZ plane
            denom = n1[1]*n2[2] - n1[2]*n2[1]
            if round(denom, 10) != 0:
                y = (d1*n2[2] - d2*n1[2]) / denom
                z = (d2*n1[1] - d1*n2[1]) / denom
                point = Point3D(0, y, z)
            else:
                # try XZ plane
                denom = n1[0]*n2[2] - n1[2]*n2[0]
                x = (d1*n2[2] - d2*n1[2]) / denom
                z = (d2*n1[0] - d1*n2[0]) / denom
                point = Point3D(x, 0, z)

        return Line3D(point, direction)