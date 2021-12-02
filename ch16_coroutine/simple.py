import inspect

def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine recieved:', x)

def simple_coro2(a):
    print('-> Started: a=', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)

def coroutine(func):
    def primer(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return primer

@coroutine
def average():
    n = 0
    total = 0.0
    average = None
    while(True):
        a = yield average
        n += 1
        total += a
        average = total/n
