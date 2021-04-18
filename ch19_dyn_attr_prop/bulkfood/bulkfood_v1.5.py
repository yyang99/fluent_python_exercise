class LineItem:

    def __init__(self, description, weight, price):
        self.description = description
        self._weight = weight
        self.price = price
    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value
        else:
            raise ValueError("value must be >0")

if __name__ == '__main__':
    raisins = LineItem('Gloden raisins', 10, 6.95)
    print(f"{raisins.subtotal()=}")
    raisins.weight = 20
    print(f"{raisins.subtotal()=}")
    print(f"{raisins.subtotal()=}")
    walnuts = LineItem('Walnuts', -10, 10)
    print(f"{walnuts.subtotal()=}")
