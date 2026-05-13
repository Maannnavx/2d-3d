from src.line import Line2D, Line3D
from src.point import Point2D, Point3D
from src.vector import Vector2D, Vector3D

def test_line_repr():
    l = Line2D(Point2D(0, 0), Vector2D(1, 1))
    assert str(l) == "Line(point=Point2D(0, 0), direction=Vector2D(1, 1))"

def test_point_at():
    l = Line2D(Point2D(0, 0), Vector2D(1, 1))
    assert l.point_at(0).coords == (0, 0)
    assert l.point_at(1).coords == (1, 1)
    assert l.point_at(2).coords == (2, 2)
    assert l.point_at(-1).coords == (-1, -1)

def test_contains_point():
    l = Line2D(Point2D(0, 0), Vector2D(1, 1))
    assert l.contains_point(Point2D(2, 2)) == True
    assert l.contains_point(Point2D(3, 4)) == False

def test_distance_to_point():
    l = Line2D(Point2D(0, 0), Vector2D(1, 0))
    assert l.distance_to_point(Point2D(3, 4)) == 4.0
    assert l.distance_to_point(Point2D(0, 0)) == 0.0

def test_is_parallel():
    l1 = Line2D(Point2D(0, 0), Vector2D(1, 0))
    l2 = Line2D(Point2D(0, 5), Vector2D(1, 0))
    l3 = Line2D(Point2D(0, 0), Vector2D(0, 1))
    assert l1.is_parallel(l2) == True
    assert l1.is_parallel(l3) == False

def test_is_perpendicular():
    l1 = Line2D(Point2D(0, 0), Vector2D(1, 0))
    l2 = Line2D(Point2D(0, 0), Vector2D(0, 1))
    l3 = Line2D(Point2D(0, 5), Vector2D(1, 0))
    assert l1.is_perpendicular(l2) == True
    assert l1.is_perpendicular(l3) == False

def test_intersection():
    l1 = Line2D(Point2D(0, 0), Vector2D(1, 0))
    l2 = Line2D(Point2D(0, 0), Vector2D(0, 1))
    l3 = Line2D(Point2D(0, 5), Vector2D(1, 0))
    assert l1.intersection(l2).coords == (0.0, 0.0)
    assert l1.intersection(l3) is None

def test_closest_points():
    l1 = Line3D(Point3D(0, 0, 0), Vector3D(1, 0, 0))
    l2 = Line3D(Point3D(0, 1, 1), Vector3D(0, 1, 0))
    result = l1.closest_points(l2)
    assert result[0].coords == (0.0, 0.0, 0.0)
    assert result[1].coords == (0.0, 0.0, 1.0)

from src.line import Line3D

def test_intersection_with_line():
    pl = Plane(Point3D(0, 0, 0), Vector3D(0, 0, 1))
    l1 = Line3D(Point3D(0, 0, 5), Vector3D(0, 0, -1))
    l2 = Line3D(Point3D(0, 0, 5), Vector3D(1, 0, 0))
    assert pl.intersection_with_line(l1).coords == (0.0, 0.0, 0.0)
    assert pl.intersection_with_line(l2) is None