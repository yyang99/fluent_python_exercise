from mirror import LookingGlass
manager = LookingGlass()
print(f'{manager=}')
what = manager.__enter__()
print('Alice, Kitty and Snowdrop')
print(what)

manager.__exit__(None, None, None)
print(f'{what=}')
print('Back to Normal')