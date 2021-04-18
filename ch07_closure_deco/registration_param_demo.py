from registration_param import *

print('*' * 30, ' [ start main ]')

print(f'{registry=}')

register()(f3)
print(f'{registry=}')

register(active=False)(f2)
print(f'{registry=}')
