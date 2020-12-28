def f(a, b):
    a += b
    return a

x = 1
y = 2
z = f(x, y)
print(f"{x=}, {y=}, {z=}")

a = [1, 2]
b = [3, 4]
c = f(a, b)
print(f"{a=}, {b=}, {c=}")