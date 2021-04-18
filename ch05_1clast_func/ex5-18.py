from ex5_10_tag import tag
import inspect
sig = inspect.signature(tag)
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
bound_args=sig.bind(**my_tag)
print(f"{bound_args=}")

for name, value in bound_args.arguments.items():
    print(name, '=', value)