from src.point import Point2D, Point3D

def test_distance_2d():
    p1 = Point2D(1, 2)
    p2 = Point2D(4, 6)
    assert p1.distance_to(p2) == 5.0

def test_distance_3d():
    p3 = Point3D(1, 2, 3)
    p4 = Point3D(4, 6, 8)
    assert round(p3.distance_to(p4), 2) == 7.07

def test_midpoint_2d():
    p1 = Point2D(1, 2)
    p2 = Point2D(4, 6)
    mid = p1.midpoint(p2)
    assert mid.coords == (2.5, 4.0)

def test_midpoint_3d():
    p3 = Point3D(1, 2, 3)
    p4 = Point3D(4, 6, 8)
    mid = p3.midpoint(p4)
    assert mid.coords == (2.5, 4.0, 5.5)