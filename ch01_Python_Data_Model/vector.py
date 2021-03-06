from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scaler):
        return Vector(self.x * scaler, self.y * scaler)

if __name__ == "__main__":
    v1 = Vector(3,4)
    print(f"{v1}")
    print(f"hypotenus = {abs(v1)}")
    print(f"{bool(v1)}")
    v2 = Vector(1, 2)
    print(v1+v2)
