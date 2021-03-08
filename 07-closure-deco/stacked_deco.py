def d1(func):
    print('*' * 50, "\nrunning in ---> d1")
    print(f'called by ---> d1({func.__name__})')
    def d1_inner(*args, **kwargs):
        print('*' * 50, "\nrunning in ---> d1_inner")
        print(f'called by ---> {d1_inner.__name__}({func.__name__}(*{args}, **{kwargs})')
        return func(*args, **kwargs)
    return d1_inner

def d2(func):
    print('*' * 50, "\nrunning in ---> d2")
    print(f'called by ---> d2({func.__name__})')
    def d2_inner(*args, **kwargs):
        print('*' * 50, "\nrunning in ---> d2_inner")
        print(f'called by ---> {d2_inner.__name__}({func.__name__}(*{args}, **{kwargs}))')
        return func(*args, **kwargs)
    return d2_inner

@d1
@d2
def f(*args, **kwargs):
    print('*' * 50, "\nrunning in ---> f")
    print(f'called by ---> {f.__name__}(*{args}, **{kwargs})')
    arg_lst = []
    arg_lst.append(', '.join(args))
    paris = [f'{k}={v}' for k,v in kwargs.items()]
    arg_lst.append(', '.join(paris))
    arg_str = ', '.join(arg_lst)
    return arg_str

if __name__ == '__main__':
    print('*' * 50, "\nrunning in ---> main")
    print(f"calling ---> {f.__name__}('Hello', 'World', ending1='!', ending2='...')")
    print(f"{f('Hello', 'World', ending1='!', ending2='...')=}")