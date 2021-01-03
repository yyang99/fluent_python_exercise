import abc

class MySized(metaclass=abc.ABCMeta):

    __slots__ = ()

    @abc.abstractmethod
    def __len__(self):
        return 0

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MySized:
            if any('__len__' in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented