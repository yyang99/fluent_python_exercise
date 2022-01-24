class Bar:
    def __set_name__(self, owner, name):
        print(f'{self} was named {name} by {owner}')

class Foo:
    x = Bar()
    y = Bar()