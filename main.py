from src.point import Point2D, Point3D

p1 = Point2D(1, 2)
p2 = Point3D(1, 2, 3)

x, y = p1
print(x, y)  # 1 2

x, y, z = p2
print(x, y, z)  # 1 2 3