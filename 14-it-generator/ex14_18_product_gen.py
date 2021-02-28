import itertools

a = itertools.product('ABC', range(2))
print(f'{list(a)=}')

suits = 'spades hearts diamonds clubs'.split()
b = itertools.product('AK', suits)
print(f'{list(b)}')

c = itertools.product('ABC')
print(f'{list(c)}')

d = itertools.product('ABC', repeat=2)
print(f'{list(d)}')

e = itertools.product(range(2), repeat=3)
print(f'{list(e)}')

rows = itertools.product('AB', range(2), repeat=2)
for row in rows: print(row)
