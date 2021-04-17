import collections


class Text(collections.UserString):

    def __repr__(self):
        return f'Text({self.data})'
    def reverse(self):
        return self[::-1]