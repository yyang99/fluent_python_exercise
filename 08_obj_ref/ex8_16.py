import weakref
s1 = {1, 2, 3}
s2 = s1
def bye():
    print("Gone with the wind ...")

ender = weakref.finalize(s1, bye)
print(f"{ender.alive}")
del s1
print(f"{ender.alive}")
s2 = 'spam'
print(f"{ender.alive}")
