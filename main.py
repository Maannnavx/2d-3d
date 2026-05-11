from src.point import Point2D, Point3D
from src.vector import Vector2D, Vector3D

v1 = Vector3D(1, 0, 0)
v2 = Vector3D(0, 1, 0)
print(v1.cross(v2))  # Vector3D(0, 0, 1) — points straight up!

v3 = Vector3D(2, 3, 4)
v4 = Vector3D(5, 6, 7)
print(v3.cross(v4))  # Vector3D(-3, 6, -3)