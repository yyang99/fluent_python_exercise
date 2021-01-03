class MyList:
    def __init__(self, in_iter):
        self.data = list(in_iter)

from array import array
mylist = MyList(array('f', [1, 2, 3]))

print(mylist.data)

class MyFields:
    def __init__(self, field_names):
        try:
            field_names = field_names.replace('.',' ').split()
        except AttributeError:
            pass
        self.field_names = tuple(field_names)

fields1 = MyFields('field1,field2,field3')
print(fields1.field_names)

fields2 = MyFields(['field1', 'field2', 'field3'])
print(fields1.field_names)
