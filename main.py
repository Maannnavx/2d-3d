from src.point import Point2D, Point3D

p1 = Point2D(3, 4)
p2 = Point3D(1, 2, 2)

print(p1.distance_to_origin())  # 5.0
print(p2.distance_to_origin())  # 3.0