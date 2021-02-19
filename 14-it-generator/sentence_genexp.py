import re
from collections import abc

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence({})'.format(repr(self.text))

    def __iter__(self):
        return (word.group() for word in RE_WORD.finditer(self.text))

if __name__ == '__main__':
    s = Sentence('this is a test sentence')
    print(s)

    for i in s:
        print(i)

    for j in s:
        print(j)

    print(f'{issubclass(Sentence, abc.Iterable)=}')
    print(f'{issubclass(Sentence, abc.Iterator)=}')
    print(f'{isinstance(s, abc.Iterable)=}')
    print(f'{isinstance(s, abc.Iterator)=}')