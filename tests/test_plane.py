from src.plane import Plane
from src.point import Point3D
from src.vector import Vector3D
from src.line import Line3D

def test_plane_repr():
    pl = Plane(Point3D(0, 0, 0), Vector3D(0, 0, 1))
    assert str(pl) == "Plane(point=Point3D(0, 0, 0), normal=Vector3D(0, 0, 1))"

def test_from_three_points():
    pl = Plane.from_three_points(
        Point3D(0, 0, 0),
        Point3D(1, 0, 0),
        Point3D(0, 1, 0)
    )
    assert pl.normal.components == (0, 0, 1)

def test_contains_point():
    pl = Plane(Point3D(0, 0, 0), Vector3D(0, 0, 1))
    assert pl.contains_point(Point3D(1, 1, 0)) == True
    assert pl.contains_point(Point3D(1, 1, 1)) == False

def test_distance_to_point():
    pl = Plane(Point3D(0, 0, 0), Vector3D(0, 0, 1))
    assert pl.distance_to_point(Point3D(0, 0, 5)) == 5.0
    assert pl.distance_to_point(Point3D(0, 0, 0)) == 0.0

def test_is_parallel():
    pl1 = Plane(Point3D(0, 0, 0), Vector3D(0, 0, 1))
    pl2 = Plane(Point3D(0, 0, 5), Vector3D(0, 0, 1))
    pl3 = Plane(Point3D(0, 0, 0), Vector3D(0, 1, 0))
    assert pl1.is_parallel(pl2) == True
    assert pl1.is_parallel(pl3) == False

def test_is_perpendicular():
    pl1 = Plane(Point3D(0, 0, 0), Vector3D(0, 0, 1))
    pl2 = Plane(Point3D(0, 0, 0), Vector3D(0, 1, 0))
    pl3 = Plane(Point3D(0, 0, 5), Vector3D(0, 0, 1))
    assert pl1.is_perpendicular(pl2) == True
    assert pl1.is_perpendicular(pl3) == False

def test_intersection_with_line():
    pl = Plane(Point3D(0, 0, 0), Vector3D(0, 0, 1))
    l1 = Line3D(Point3D(0, 0, 5), Vector3D(0, 0, -1))
    l2 = Line3D(Point3D(0, 0, 5), Vector3D(1, 0, 0))
    assert pl.intersection_with_line(l1).coords == (0.0, 0.0, 0.0)
    assert pl.intersection_with_line(l2) is None

def test_intersection_with_plane():
    pl1 = Plane(Point3D(0, 0, 0), Vector3D(0, 0, 1))
    pl2 = Plane(Point3D(0, 0, 0), Vector3D(0, 1, 0))
    pl3 = Plane(Point3D(0, 0, 5), Vector3D(0, 0, 1))
    
    result = pl1.intersection_with_plane(pl2)
    assert result is not None
    assert result.direction.components == (-1, 0, 0)
    assert pl1.intersection_with_plane(pl3) is None