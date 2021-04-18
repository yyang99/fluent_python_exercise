def quantity():
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0

    storage_name = f"_{quantity}:{quantity.counter}"

    def qty_getter(instance):
        return getattr(instance, storage_name)

    def qty_setter(instance, value):
        if value > 0:
            setattr(instance, storage_name, value)

    return property(qty_getter, qty_setter)


class LineItem:
    weight = quantity()
    price = quantity()

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
