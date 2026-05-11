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

def test_eq():
    p1 = Point2D(1, 2)
    p2 = Point2D(1, 2)
    p3 = Point2D(3, 4)
    assert p1 == p2
    assert p1 != p3

def test_len():
    p1 = Point2D(1, 2)
    p2 = Point3D(1, 2, 3)
    assert len(p1) == 2
    assert len(p2) == 3

def test_iter():
    p1 = Point2D(1, 2)
    x, y = p1
    assert x == 1
    assert y == 2

def test_distance_to_origin():
    p1 = Point2D(3, 4)
    p2 = Point3D(1, 2, 2)
    assert p1.distance_to_origin() == 5.0
    assert p2.distance_to_origin() == 3.0