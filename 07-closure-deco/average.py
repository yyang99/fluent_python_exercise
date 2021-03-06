def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

avg = make_averager()
print(f'{avg(10)}')
print(f'{avg(11)}')
print(f'{avg(12)}')

print(f'{avg.__code__.co_varnames=}')
print(f'{avg.__code__.co_freevars=}')

print(f'{avg.__closure__=}')
print(f'{avg.__closure__[0].cell_contents=}')