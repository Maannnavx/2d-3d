from src.line import Line2D, Line3D
from src.point import Point2D, Point3D
from src.vector import Vector2D, Vector3D

l1 = Line2D(Point2D(0, 0), Vector2D(1, 0))
l2 = Line2D(Point2D(0, 5), Vector2D(1, 0))
l3 = Line2D(Point2D(0, 0), Vector2D(0, 1))

print(l1.distance_to_point(Point2D(3, 4)))  # 4.0
print(l1.distance_to_point(Point2D(0, 0)))  # 0.0

print(l1.is_parallel(l2))      # True
print(l1.is_parallel(l3))      # False

print(l1.is_perpendicular(l3)) # True
print(l1.is_perpendicular(l2)) # False