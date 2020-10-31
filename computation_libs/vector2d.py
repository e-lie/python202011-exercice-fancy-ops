"""
A 2-dimensional vector class from the fluent python book chapter 9
"""

from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


if __name__ == "__main__":
    
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    x, y = v1
    x, y
    v1
    v1_clone = eval(repr(v1))
    v1 == v1_clone
    print(v1)
    octets = bytes(v1)
    octets
    abs(v1)
    bool(v1), bool(Vector2d(0, 0))

    # Test of ``.frombytes()`` class method:

    v1_clone = Vector2d.frombytes(bytes(v1))
    v1_clone
    v1 == v1_clone

    # Tests of ``format()`` with Cartesian coordinates:

    format(v1)
    format(v1, '.2f')
    format(v1, '.3e')

    # Tests of the ``angle`` method::

    Vector2d(0, 0).angle()
    Vector2d(1, 0).angle()
    epsilon = 10**-8
    abs(Vector2d(0, 1).angle() - math.pi/2) < epsilon
    abs(Vector2d(1, 1).angle() - math.pi/4) < epsilon

    # Tests of ``format()`` with polar coordinates:

    format(Vector2d(1, 1), 'p')  # doctest:+ELLIPSIS
    format(Vector2d(1, 1), '.3ep')
    format(Vector2d(1, 1), '0.5fp')

    # Tests of `x` and `y` read-only properties:

    v1.x, v1.y
    # v1.x = 123 # -> raises AttributeError !

    # Tests of hashing:

    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    hash(v1), hash(v2)
    len(set([v1, v2]))