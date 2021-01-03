
from array import array
import functools
import operator
import reprlib
import math
import numbers
import itertools

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
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        # hashes = (hash(x) for x in self._components)
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)

    # def __abs__(self):
    #     return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._components[item])
        elif isinstance(item, numbers.Integral):
            return self._components[item]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos <= len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self,name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error=''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_sepc=''):
        if fmt_sepc.endswith('h'):
            fmt_sepc = fmt_sepc[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_sepc) for c in coords)
        return outer_fmt.format(', '.join(components))

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            return Vector(x + y for x, y in itertools.zip_longest(self, other, fillvalue=0.0))
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, scaler):
        if isinstance(scaler, numbers.Real):
            return Vector(n * scaler for n in self)
        else:
            raise NotImplemented

    def __rmul__(self, scaler):
        return self * scaler

    def __matmul__(self, other):
        try:
            return sum(a * b for a, b in zip(self, other))
        except TypeError:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other

if __name__ == '__main__':
    v1 = Vector([1, 2, 3])

    print(f"{v1 * 10=}")
    print(f"{v1 * 10}")


    print(f"{11 * v1=}")
    print(f"{11 * v1}")

    print(f"True * v1={True * v1}")
    print(f"False * v1={False * v1}")

    from fractions import Fraction
    print(f"v1 * Fraction(1, 3)={v1 * Fraction(1, 3)}")

    va = Vector([1, 2, 3])
    vb = Vector([5, 6, 7])

    print (f"{va @ vb == 38=}")

    print (f"{[10, 20, 30] @ vb=}")

    va @ 3