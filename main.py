from src.point import Point2D, Point3D

# Create some points
p1 = Point2D(1, 2)
p2 = Point2D(4, 6)

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Distance: {p1.distance_to(p2)}")

# 3D
p3 = Point3D(1, 2, 3)
p4 = Point3D(4, 6, 8)

print(f"Point 3: {p3}")
print(f"Point 4: {p4}")
print(f"Distance: {p3.distance_to(p4)}")