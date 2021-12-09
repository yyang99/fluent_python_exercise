from collections import namedtuple

Result = namedtuple('Result', 'count average')

def average():
    n = 0
    total = 0.0
    average = None
    while(True):
        term = yield
        if term is None:
            break
        total += term
        n += 1
        average = total/n
    return Result(n, average)

