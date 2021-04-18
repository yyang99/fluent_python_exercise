class Quantity:
    __counter = 0

    def __init__(self):
        self.cls = self.__class__
        self.prefix = self.cls.__name__
        self.index = self.cls.__counter
        self.storage_name = f"__{self.prefix}#{self.index}"
        self.cls.__counter += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value mast be >0')


class LineItem:
    weight = Quantity()
    price = Quantity()

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
