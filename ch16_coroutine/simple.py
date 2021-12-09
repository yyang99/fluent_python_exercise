
'''
>>> coro_avg = average()
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(coro_avg)
'GEN_SUSPENDED'
>>> coro_avg.send(10)
10.0
>>> coro_avg.send(30)
20.0
>>> coro_avg.send(5)
15.0
'''

import inspect
from coroutine import coroutine

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


