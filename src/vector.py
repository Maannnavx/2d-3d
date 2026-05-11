import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector{len(self.components)}D{self.components}"

    def __len__(self):
        return len(self.components)

    def __iter__(self):
        return iter(self.components)

    def __eq__(self, other):
        return self.components == other.components
    
    def magnitude(self):
        return math.sqrt(sum(c**2 for c in self.components))
    
    def __add__(self, other):
        new_components = tuple(a + b for a, b in zip(self.components, other.components))
        return Vector(*new_components)
    
    def __sub__(self, other):
        new_components = tuple(a - b for a, b in zip(self.components, other.components))
        return Vector(*new_components)
    
    def __mul__(self, scalar):
        new_components = tuple(c * scalar for c in self.components)
        return Vector(*new_components)
    
    def dot(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))


class Vector2D(Vector):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y


class Vector3D(Vector):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z

    def cross(self, other):
        return Vector3D(
        (self.y * other.z) - (self.z * other.y),
        (self.z * other.x) - (self.x * other.z),
        (self.x * other.y) - (self.y * other.x))