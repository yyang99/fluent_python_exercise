### auxiliary functions for display only ###
def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return f'<class {obj.__name__}>'
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return f'<{cls_name(obj)} object>'


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print(f'-> {cls_name(args[0])}.__{name}__({pseudo_args})')


### essential classes for this example ###

class Overriding:
    """a.k.a. data descriptor or enforced descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:
    """an overriding descriptor without ``__get__``"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:
    """a.k.a. non-data or shadowable descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))

if __name__ == '__main__':
    obj = Managed()
    print('before obj.non_over = 7 ===> ', obj.non_over)
    obj.non_over = 7
    print('aftger obj.non_over = 7 ===> ', obj.non_over)

    print('before obj.over_no_get = 9 ===> ', obj.over_no_get)
    obj.over_no_get = 9 # the over_no_get.__set__ only print not really set variable
    print('aftger obj.over_no_get = 9 (note no set instance attribute in __set__) ===> ', obj.over_no_get) # note this do not have instance attribute set from previous step
    obj.__dict__['over_no_get'] = 9
    print("obj.__dict__['over_no_get'] = 9 ===> ", obj.over_no_get)
