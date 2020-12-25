brl = 1/2.43

print(f"{brl=}")

brl1 = format(brl, '0.4f')
print(f"{brl1=}")

brl2 = '{:0.4f}'.format(brl)
print(f"{brl2=}")

brl3 = '1 BRL = {rate:0.2f} USD'.format(rate=brl)
print(f"{brl3=}")