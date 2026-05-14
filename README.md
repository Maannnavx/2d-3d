# 2D & 3D Geometry Library

A custom Python library for 2D and 3D geometry operations built from scratch.
Includes data types for Points, Vectors, Lines, and Planes with a full suite of geometric operations.

---

## Project Structure
2d-3d/
├── src/
│   ├── point.py      # Point2D, Point3D
│   ├── vector.py     # Vector2D, Vector3D
│   ├── line.py       # Line2D, Line3D
│   └── plane.py      # Plane
├── tests/
│   ├── test_point.py
│   ├── test_vector.py
│   ├── test_line.py
│   └── test_plane.py
├── main.py
└── requirements.txt

---

## Installation

```bash
git clone git@github.com:Maannnavx/2d-3d.git
cd 2d-3d
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

---

## Usage

### Point

```python
from src.point import Point2D, Point3D

p1 = Point2D(1, 2)
p2 = Point2D(4, 6)

p1.distance_to(p2)        # 5.0
p1.midpoint(p2)           # Point2D(2.5, 4.0)
p1.distance_to_origin()   # 2.23...
p1 == p2                  # False
len(p1)                   # 2
x, y = p1                 # unpack
```

### Vector

```python
from src.vector import Vector2D, Vector3D

v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

v1 + v2                   # Vector2D(4, 6)
v1 - v2                   # Vector2D(-2, -2)
v1 * 3                    # Vector2D(3, 6)
v1.magnitude()            # 2.23...
v1.dot(v2)                # 11

# cross product (3D only)
v3 = Vector3D(1, 0, 0)
v4 = Vector3D(0, 1, 0)
v3.cross(v4)              # Vector3D(0, 0, 1)
```

### Line

```python
from src.line import Line2D, Line3D
from src.point import Point2D, Point3D
from src.vector import Vector2D, Vector3D

l1 = Line2D(Point2D(0, 0), Vector2D(1, 0))
l2 = Line2D(Point2D(0, 0), Vector2D(0, 1))

l1.point_at(3)                    # Point2D(3, 0)
l1.contains_point(Point2D(3, 0))  # True
l1.distance_to_point(Point2D(3, 4)) # 4.0
l1.is_parallel(l2)                # False
l1.is_perpendicular(l2)           # True
l1.intersection(l2)               # Point2D(0, 0)

# closest points between two 3D lines
l3 = Line3D(Point3D(0, 0, 0), Vector3D(1, 0, 0))
l4 = Line3D(Point3D(0, 1, 1), Vector3D(0, 1, 0))
l3.closest_points(l4)             # (Point3D(0,0,0), Point3D(0,0,1))
```

### Plane

```python
from src.plane import Plane
from src.point import Point3D
from src.vector import Vector3D

# create from point and normal
pl1 = Plane(Point3D(0, 0, 0), Vector3D(0, 0, 1))

# create from three points
pl2 = Plane.from_three_points(
    Point3D(0, 0, 0),
    Point3D(1, 0, 0),
    Point3D(0, 1, 0)
)

pl1.contains_point(Point3D(1, 1, 0))    # True
pl1.distance_to_point(Point3D(0, 0, 5)) # 5.0
pl1.is_parallel(pl2)                    # True
pl1.is_perpendicular(pl2)               # False

# intersection with a line
from src.line import Line3D
l = Line3D(Point3D(0, 0, 5), Vector3D(0, 0, -1))
pl1.intersection_with_line(l)           # Point3D(0, 0, 0)

# intersection with another plane (returns a Line3D)
pl3 = Plane(Point3D(0, 0, 0), Vector3D(0, 1, 0))
pl1.intersection_with_plane(pl3)        # Line3D along X axis
```

---

## Running Tests

```bash
python -m pytest tests/ -v
```

---

## Built With

- Python 3.13
- pytest

