from tombola import Tombola
from bingo import BingoCage

class AddableBingoCage(BingoCage):

        def __add__(self, other):
            if isinstance(other, Tombola):
                return AddableBingoCage(self.inspect() + other.inspect())
            else:
                return NotImplemented

        def __iadd__(self, other):
            if isinstance(other, Tombola):
                other_iterable = other.inspect()
            else:
                try:
                    other_iterable = iter(other)
                except TypeError:
                    self_cls = type(self).__name__
                    msg="right operend in += must be {!r} or an iterable"
                    raise TypeError(msg.format(self_cls))
            self.load(other_iterable)
            return self
def test_add_iadd():
    vowels = 'AEIOU'
    globe = AddableBingoCage(vowels)
    print(f"{globe.inspect()=}")
    print(f"{globe.pick()=}")
    print(f"{len(globe.inspect())=}")

    globe2 = AddableBingoCage('XYZ')
    globe3 = globe + globe2
    print(f"{globe3.inspect()=}")
    print(f"{len(globe3.inspect())=}")

    # void = globe + [10, 20]

    globe_orig = globe
    print(f"{len(globe.inspect())}")

    globe += globe2
    print(f"{len(globe.inspect())}")

    globe += ['M', 'N']
    print(f"{len(globe.inspect())}")

    print(f"{globe_orig is globe=}")

    globe += 1

if __name__ == '__main__':
    test_add_iadd()
