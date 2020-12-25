t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print(f"{t1 == t2=}")

print(f"{id(t1[-1])=}")

t1[-1].append(99)

print(f"{t1=}")

print(f"{id(t1[-1])=}")

print(f"{t1 == t2=}")

