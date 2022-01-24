class Lazy:
    def __init__(self, func):
        self.func = func

    def __set_name__(self, owner, name):
        self.key = name

    def __get__(self, instance, cls):
        if instance:
            print(f"calculating {self.func}({instance})")
            value = self.func(instance)
            instance.__dict__[self.key] = value
            return value
        else:
            return self.func

class Rectangle:
    area = Lazy(lambda self: self.width * self.height)
    perimeter = Lazy(lambda self: 2 * (self.width + self.height))

    def __init__(self, width, height):
        self.width = width
        self.height = height

a = Rectangle(2, 3)

'''
>>> a.__dict__
{'width': 2, 'height': 3}
>>> Rectangle.area
<function Rectangle.<lambda> at 0x10aedc7b8>
>>> a.area
calculating <function Rectangle.<lambda> at 0x10aedc7b8>(<__main__.Rectangle object at 0x10b033390>)
6
>>> a.__dict__
{'width': 2, 'height': 3, 'area': 6}
>>> a.area
6
>>> a.area
6
'''