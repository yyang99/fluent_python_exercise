with open('README.rst') as fp:
    src = fp.read(60)

print(f'{len(src)=}')

print(f'{type(fp)=}')
print(f'{dir(fp)=}')
print(f'{(fp.closed, fp.encoding)=}')