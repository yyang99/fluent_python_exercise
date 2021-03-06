import time
from clockdeco2 import clock

@clock
def snooze(seconds, **kwargs):
    ''' snooze func'''
    time.sleep(seconds)

@clock
def factorial(n, **kwargs):
    ''' factorial func '''
    return 1 if n < 2 else n * factorial(n-1, **kwargs)

if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123, a=1, b=2)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6, c=3, d=4))