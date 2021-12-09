def chain(*iterables):
    for it in iterables:
        yield from it

s = 'ABC'
t = tuple(range(3))
print(f"{list(chain(s,t))=}")
