from typing import Any, Iterator


def vowel(c):
    return c.lower() in 'aeiou'

a = filter(vowel, 'Aardvark')
print(f'{list(a)=}')

import itertools

b = itertools.filterfalse(vowel, 'Aardvark')
print(f'{list(b)=}')

c = itertools.dropwhile(vowel, 'Aardvark')
print(f'{list(c)=}')

d: Iterator[Any] = itertools.takewhile(vowel, 'Aardvark')
print(f'{list(d)=}')

e = itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1))
print(f'{list(e)=}')

f = itertools.islice('Aardvark', 4)
print(f'{list(f)=}')

g = itertools.islice('Aardvark', 4, 7)
print(f'{list(g)=}')

h = itertools.islice('Aardvark', 1, 7, 2)
print(f'{list(h)=}')
