class HauntedBus:
    '''A bus model haunted by ghost passengers'''

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus2 = HauntedBus()
print(f"{bus2.passengers=}")
bus2.pick('Carrie')
print(f"{bus2.passengers=}")
bus3 = HauntedBus()
print(f"{bus3.passengers=}")
print(f"{id(bus2.passengers)=}, {id(bus3.passengers)=}")

print(f'{bus2.passengers is HauntedBus.__init__.__defaults__[0]=}')
print(f'{bus3.passengers is HauntedBus.__init__.__defaults__[0]=}')