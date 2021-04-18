from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
print(f"{upcase(s)=}")
print(f"{methodcaller('upper')(s)=}")
print(f"{s.upper()=}")