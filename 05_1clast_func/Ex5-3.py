def fact(n):
    return 1 if n <2 else n * fact(n-1)

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

print(sorted(fruits, key=len))

def reverse(work):
    return work[::-1]

print(reverse('testing'))

a = list(map(fact, range(6)))
a1 = [fact(i) for i in range(6)]

print(f"{a=}")
print(f"{a1=}")

b = list(map(fact, filter(lambda x: x % 2, range(6))))
b1 = [fact(i) for i in range(6) if i %2]

print(f'{b=}')
print(f'{b1=}')

