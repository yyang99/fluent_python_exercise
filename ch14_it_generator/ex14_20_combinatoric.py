import itertools

a = itertools.combinations('ABC', 2)
print(f'combination: {list(a)=}')

b = itertools.combinations_with_replacement('ABC', 2)
print(f'combination_with_replacement: {list(b)=}')

c = itertools.permutations('ABC', 2)
print(f'permunation: {list(c)=}')

d = itertools.product('ABC', repeat=2)
print(f'product: {list(d)=}')