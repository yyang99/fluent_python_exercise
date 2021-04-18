class LineItem:

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
    def subtotal(self):
        return self.weight * self.price

    def get_weight(self):
        return self._weight

    def set_weight(self, value):
        if value > 0:
            self._weight = value
        else:
            raise ValueError("value must be >0")

    weight = property(get_weight, set_weight)

if __name__ == '__main__':
    raisins = LineItem('Gloden raisins', 10, 6.95)
    print(f"{raisins.subtotal()=}")
    raisins.weight = 20
    print(f"{raisins.subtotal()=}")
