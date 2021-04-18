sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

import itertools

a = itertools.accumulate(sample)
print(f'{list(a)=}')

b = itertools.accumulate(sample, min)
print(f'{list(b)=}')

c = itertools.accumulate(sample, max)
print(f'{list(c)=}')

import operator

d = itertools.accumulate(sample, operator.mul)
print(f'{list(d)=}')

e = itertools.accumulate(range(1, 11), operator.mul)
print(f'{list(e)=}')
