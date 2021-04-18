s = 'café'
print(f'{len(s)=}')
print(f'{s=}')

b = s.encode('utf8')
print(f'{len(b)=}')
print(f'{b=}')

c = b.decode('utf8')
print(f'{len(c)=}')
print(f'{c=}')