from operator import mul
from functools import partial
triple = partial(mul, 3)
print(f"{triple(3)=}")

a = list(map(triple, range(1,10)))
print(a)