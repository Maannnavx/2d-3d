from src.plane import Plane
from src.point import Point2D, Point3D
from src.line import Line2D, Line3D
from src.vector import Vector2D, Vector3D

pl = Plane(Point3D(0, 0, 0), Vector3D(0, 0, 1))

print(pl.contains_point(Point3D(1, 1, 0)))   # True
print(pl.contains_point(Point3D(1, 1, 1)))   # False

print(pl.distance_to_point(Point3D(0, 0, 5)))  # 5.0
print(pl.distance_to_point(Point3D(0, 0, 0)))  # 0.0

pl2 = Plane(Point3D(0, 0, 5), Vector3D(0, 0, 1))
pl3 = Plane(Point3D(0, 0, 0), Vector3D(0, 1, 0))

print(pl.is_parallel(pl2))      # True
print(pl.is_parallel(pl3))      # False
print(pl.is_perpendicular(pl3)) # True
print(pl.is_perpendicular(pl2)) # False