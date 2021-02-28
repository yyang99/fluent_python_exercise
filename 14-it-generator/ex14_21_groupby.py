import itertools
a = itertools.groupby('LLLLAAGG')
print(f'groupby: {list(a)=}')

for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)
print(f'{animals=}')

for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))

for length, group in itertools.groupby(reversed(animals), len):
    print('reversed(animals): ',length , '->', list(group))