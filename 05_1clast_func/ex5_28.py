from ex5_10_tag import tag
print(tag)
from functools import partial
picture = partial(tag, 'img', cls='pic-frame')

print(picture)
print(picture(src='wumpus.jpg'))
print(picture.func)
print(picture.args)
print(picture.keywords)