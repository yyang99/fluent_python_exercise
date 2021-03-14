cafe = bytes('café', encoding='utf_8')
print(f'{cafe=}')
print(f'{cafe[0]=}')
print(f'{cafe[:1]=}')

cafe_arr = bytearray(cafe)
print(f'{cafe_arr=}')
print(f'{cafe_arr[-1:]=}')

