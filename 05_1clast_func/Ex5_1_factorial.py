def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)

print(factorial(42))

a = map(factorial, range(11))

print(a)

print(list(a))