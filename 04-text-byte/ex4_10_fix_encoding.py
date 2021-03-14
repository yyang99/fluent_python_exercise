fp = open('cafe.txt', 'w', encoding='utf-8')
print(f"{fp=}")
print(f"{fp.write('café')=}")
fp.close()
import os
print(f"{os.stat('cafe.txt').st_size=}")

fp2 = open('cafe.txt')
print(f"{fp2=}")
print(f"{fp2.encoding=}")
print(f"{fp2.read()=}")

fp3 = open('cafe.txt', encoding='utf_8')
print(f"{fp3=}")
print(f"{fp3.read()=}")

fp4 = open('cafe.txt', 'rb')
print(f"{fp4=}")
print(f"{fp4.read()=}")
