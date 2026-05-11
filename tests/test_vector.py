from src.vector import Vector2D, Vector3D

def test_repr():
    v = Vector2D(3, 4)
    assert str(v) == "Vector2D(3, 4)"

def test_len():
    v = Vector2D(3, 4)
    assert len(v) == 2

def test_eq():
    v1 = Vector2D(3, 4)
    v2 = Vector2D(3, 4)
    v3 = Vector2D(1, 2)
    assert v1 == v2
    assert v1 != v3

def test_magnitude():
    v1 = Vector2D(3, 4)
    v2 = Vector3D(1, 2, 2)
    assert v1.magnitude() == 5.0
    assert v2.magnitude() == 3.0

def test_add():
    v1 = Vector2D(1, 2)
    v2 = Vector2D(3, 4)
    assert (v1 + v2).components == (4, 6)

def test_sub():
    v1 = Vector2D(5, 6)
    v2 = Vector2D(2, 3)
    assert (v1 - v2).components == (3, 3)

def test_mul():
    v1 = Vector2D(2, 3)
    assert (v1 * 3).components == (6, 9)