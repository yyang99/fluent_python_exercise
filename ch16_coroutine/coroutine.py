from functools import wraps

def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return primer
    pass

