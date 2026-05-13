from src.line import Line2D, Line3D
from src.point import Point2D, Point3D
from src.vector import Vector2D, Vector3D

l = Line2D(Point2D(0, 0), Vector2D(1, 1))

print(l.contains_point(Point2D(2, 2)))   # True
print(l.contains_point(Point2D(3, 4)))   # False