import itertools

ct = itertools.count()
print(f'{next(ct)=}')

print(f'{(next(ct), next(ct), next(ct))=}')

a = itertools.islice(itertools.count(1, .3), 3)
print(f'{list(a)}')

cy = itertools.cycle('ABC')
print(f'{next(cy)=}')

b = itertools.islice(cy, 7)
print(f'{list(b)=}')

rp = itertools.repeat(8, 4)
print(f'{list(rp)=}')

import operator

c = map(operator.mul, range(11), itertools.repeat(5))
print(f'{list(c)=}')
