city = 'São Paulo'
print(f"{city.encode('utf-8')=}")
print(f"{city.encode('utf-16')=}")
print(f"{city.encode('iso8859_1')=}")
print(f"{city.encode('cp437', errors='ignore')=}")
print(f"{city.encode('cp437', errors='replace')=}")
print(f"{city.encode('cp437', errors='xmlcharrefreplace')=}")