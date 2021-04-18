def quantity(storage_name):
    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value

    return property(qty_getter, qty_setter)

class LineItem:
    weight = quantity('weight')
    price = quantity('price')
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price


if __name__ == '__main__':
    nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
    print(f"{nutmeg.weight, nutmeg.price=}")
    print(f'{sorted(vars(nutmeg).items())}')
