import re
from collections import abc

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence({})\nWords({})'.format(repr(self.text), repr(self.words))

    def __iter__(self):
        for word in self.words:
            yield word
        return

if __name__ == '__main__':
    s = Sentence('this is a test sentence')

    for i in s:
        print(i)

    for j in s:
        print(j)

    print(f'{issubclass(Sentence, abc.Iterable)=}')
    print(f'{issubclass(Sentence, abc.Iterator)=}')
    print(f'{isinstance(s, abc.Iterable)=}')
    print(f'{isinstance(s, abc.Iterator)=}')