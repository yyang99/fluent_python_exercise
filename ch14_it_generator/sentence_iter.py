import re
import reprlib
from collections import abc

RE_WORD = re.compile('\w+')
class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return '''
===========================[{}]
Sentence({})
Words({})
==========================='''.format(type(self), repr(self.text), repr(self.words))

    def __iter__(self):
        return SentenceIterator(self.words)

class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0


    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    # def __iter__(self):
    #     return self

class SentenceIterator1(abc.Iterator):
    def __init__(self, words):
        self.words = words
        self.index = 0


    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

if __name__ == '__main__':
    s = Sentence("this is a test sentence")
    print(s)
    print(f'{issubclass(Sentence, abc.Iterable)=}')
    print(f'{issubclass(Sentence, abc.Iterator)=}')
    print(f'{issubclass(SentenceIterator, abc.Iterable)=}')
    print(f'{issubclass(SentenceIterator, abc.Iterator)=}')
    print(f'{issubclass(SentenceIterator1, abc.Iterable)=}')
    print(f'{issubclass(SentenceIterator1, abc.Iterator)=}')
    print(f'{isinstance(s, abc.Iterable)=}')
    print(f'{isinstance(s, abc.Iterable)=}')