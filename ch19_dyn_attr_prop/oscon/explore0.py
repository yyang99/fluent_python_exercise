from collections import abc


class FrozenJSON:
    """ A read-only for navigating a JSON-like object
        using attribute notion
    """

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

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
    print(f"{talk.flavour=}")


