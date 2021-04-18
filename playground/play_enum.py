from enum import Enum

class YesNo(str, Enum):
    yes = 'yes'
    no = 'no'

a = YesNo.yes

b = YesNo('yes')

print(a, b)