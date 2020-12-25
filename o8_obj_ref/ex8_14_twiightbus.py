class TwilightBus:
    def __init__(self, passengers:list=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
print(f"{basketball_team=}")