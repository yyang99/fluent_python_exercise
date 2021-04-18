from collections import abc
from keyword import iskeyword

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
        self.__data = {}
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])


if __name__ == '__main__':
    from osconfeed import load
    raw_feed = load()
    feed = FrozenJSON(raw_feed)
    print(f"{len(feed.Schedule.keys())=}")

    for key, value in sorted(feed.Schedule.items()):
        print('{:3} {}'.format(len(value), key))

    print(f"{feed.Schedule.speakers[-1].name=}")

    talk = feed.Schedule.events[40]

    print(f"{type(talk)=}")
    print(f"{talk.name=}")
    print(f"{talk.speakers=}")
