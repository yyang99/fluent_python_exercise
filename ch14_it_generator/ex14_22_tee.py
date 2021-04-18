import itertools
print(f"{list(itertools.tee('ABC'))=}")

g1, g2 = itertools.tee('ABC')

print(f"{next(g1)=}")
print(f"{next(g1)=}")
print(f"{next(g2)=}")
print(f"{next(g2)=}")

a = zip(*itertools.tee('ABC'))
print(f'{list(a)=}')