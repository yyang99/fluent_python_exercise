s = 'ABC'
print(f'{s=}')
print('-----------[for loop]')
for char in s:
    print(char)

print('-----------[iterator and next]')

it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
