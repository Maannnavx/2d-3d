from src.point import Point2D, Point3D

p1 = Point2D(1, 2)
p2 = Point2D(4, 6)
print(f"Midpoint 2D: {p1.midpoint(p2)}")

p3 = Point3D(1, 2, 3)
p4 = Point3D(4, 6, 8)
print(f"Midpoint 3D: {p3.midpoint(p4)}")