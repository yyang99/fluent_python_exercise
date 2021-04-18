class Foo:

    @property
    def bar(self):
        '''The bar attribute'''
        return self.__dict__['bar']

    @bar.setter
    def bar(self, value):
        self.__dict__['bar'] = value

if __name__ == '__main__':
    print(f'{help(Foo.bar)}')
    print(f'{help(Foo)}')