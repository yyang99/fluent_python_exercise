class Quantity:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value mast be >0')


class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    raisins = LineItem('Gloden raisins', 10, 6.95)
    print(f"{raisins.subtotal()=}")
    raisins.weight = 20
    print(f"{raisins.subtotal()=}")
