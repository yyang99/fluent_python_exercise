class Foo:
    def __init__(self):
        self._a = list(range(0,30,10))
    def __getitem__(self, pos):
        return self._a[pos]
    # def __iter__(self):
    #     return (i for i in self._a)

f = Foo()
print(f[1])

for i in f:
    print(i)

print(f"{20 in f=}")
print(f"{15 in f=}")

class Building(object):
    def __init__(self, floors):
        self._floors = [None] * floors

    def __setitem__(self, floor_number, data):
        self._floors[floor_number] = data

    def __getitem__(self, floor_number):
        return self._floors[floor_number]


building1 = Building(4)  # Construct a building with 4 floors
building1[0] = 'Reception'
building1[1] = 'ABC Corp'
building1[2] = 'DEF Inc'
print(building1[2])