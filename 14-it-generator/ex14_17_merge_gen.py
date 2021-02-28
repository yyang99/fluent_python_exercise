import itertools

a = itertools.chain('ABC', range(2))
print(f'{list(a)=}')

b = itertools.chain.from_iterable(enumerate('ABC'))
print(f'{list(b)=}')

c = zip('ABC', range(5))
print(f'{list(c)=}')

d = zip('ABC', range(5), [10, 20, 30, 40])
print(f'{list(d)=}')

e = itertools.zip_longest('ABC', range(5))
print(f'{list(e)}')

f = itertools.zip_longest('ABC', range(5), fillvalue='?')
print(f'{list(f)}')