octets = b'Montr\xe9al'
print(f"{octets.decode('cp1252')=}")
print(f"{octets.decode('iso8859_7')=}")
print(f"{octets.decode('koi8_R')=}")
print(f"{octets.decode('utf-8', errors='replace')=}")


