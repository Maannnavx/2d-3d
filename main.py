from src.plane import Plane
from src.point import Point2D, Point3D
from src.line import Line2D, Line3D
from src.vector import Vector2D, Vector3D

pl1 = Plane(Point3D(0, 0, 0), Vector3D(0, 0, 1))  # XY plane
pl2 = Plane(Point3D(0, 0, 0), Vector3D(0, 1, 0))  # XZ plane
pl3 = Plane(Point3D(0, 0, 5), Vector3D(0, 0, 1))  # parallel to pl1

print(pl1.intersection_with_plane(pl2))  # a Line3D along X axis
print(pl1.intersection_with_plane(pl3))  # None — parallel planes