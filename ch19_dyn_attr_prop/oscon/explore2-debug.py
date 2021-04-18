from collections import abc


class FrozenJSON:
    """ A read-only for navigating a JSON-like object
        using attribute notion
    """

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])


if __name__ == '__main__':
    data = FrozenJSON(9)
    print(f"{data=}")

    raw_feed = {
        'a': 1,
        'b': [{'b1': 21}, {'b2': 22}],
        'c': {'c1': 31, 'c2': 32}
    }
    feed = FrozenJSON(raw_feed)
    print(f"{feed=}")

    a = feed.a
    b = feed.b
    c = feed.c

    print(f"{a=}")
    print(f"{b=}")
    print(f"{c=}")

    print(f"{feed.b[0].b1=}")
    print(f"{feed.c.c1=}")

    print("end")