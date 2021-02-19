class ArithmeticProgression:
    def __init__(self, begin, step, stop=None):
        self.begin = begin
        self.step = step
        self.stop = stop

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.stop is None
        index = 0
        while forever or result < self.stop:
            yield result
            index += 1
            result = self.begin + self.step * index

if __name__ == '__main__':
    ap = ArithmeticProgression(0, 1, 3)
    print(f'{list(ap)=}')
    ap = ArithmeticProgression(1, .5, 3)
    print(f'{list(ap)=}')
    ap = ArithmeticProgression(0, 1/3, 1)
    print(f'{list(ap)=}')
    from fractions import Fraction
    ap = ArithmeticProgression(0, Fraction(1, 3), 1)
    print(f'{list(ap)=}')
    from decimal import Decimal
    ap = ArithmeticProgression(0, Decimal('0.1'), .3)
    print(f'{list(ap)=}')
