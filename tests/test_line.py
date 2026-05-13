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