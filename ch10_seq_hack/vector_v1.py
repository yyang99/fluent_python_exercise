from array import array
import reprlib
import math

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        # raise NameError('something wrong')
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return('Vector({})'.format(components))

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(x * x for x in self._components)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v1 = Vector([1, 2, 3])
    v2 = Vector.frombytes(bytes(v1))

    print(f"{v1=}")
    print(f"{v1}")


    print(f"{v2=}")
    print(f"{v2}")

    print(f"{v1 == v2=}")