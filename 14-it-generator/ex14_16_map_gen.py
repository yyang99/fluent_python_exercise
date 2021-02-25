a = enumerate('albatroz', 1)
print(f'{list(a)=}')

import operator
b = map(operator.mul, range(11), range(11))
print(f'{list(b)=}')

c = map(operator.mul, range(11), [2, 4, 8])
print(f'{list(c)=}')

d = map(lambda a, b: (a, b), range(11), [2, 4, 8])
print(f'{list(d)=}')

import itertools
e = itertools.starmap(operator.mul, enumerate('albatroz', 1))
print(f'{list(e)=}')

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
f = itertools.starmap(lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1))
print(f'{list(f)=}')
