from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(f'{d_proxy[1]=}')
# d_proxy[1] = 'B'
d[2] = 'B'
print(d_proxy)