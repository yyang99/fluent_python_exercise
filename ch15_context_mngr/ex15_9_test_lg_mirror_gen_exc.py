from mirror_gen_exc import looking_glass
with looking_glass() as what:
    print('Alice, Kitty and Snowdrop')
    raise(RuntimeError)
    print(what)

print('Back to normal')
print(f'{what=}')
