class DemoException(Exception):
    """ An excption type for the demostration."""

def demo_exc_handleing():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continue...')
            else:
                print('-> coroutine received: {!r}'.format(x))
        raise RuntimeError('This line should never run.')
    finally:
        print('-> coroutine ending')
