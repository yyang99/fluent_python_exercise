class Bus:
    def __init__(self, passengers:list=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)

import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus2)
print(f"{id(bus1)=}, {id(bus2)=}, {id(bus3)=}")
print(f"{id(bus1.passengers)=}, {id(bus2.passengers)=}, {id(bus3.passengers)=}")

bus1.drop('Bill')
print(f"{bus1.passengers=}")
print(f"{bus2.passengers=}")
print(f"{bus3.passengers=}")