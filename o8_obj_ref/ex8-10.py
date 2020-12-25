a = [10, 20]
b = [a, 30]
a.append(b)
print(f"{a=}")
import copy
c = copy.deepcopy(a)
print(f"{c=}")