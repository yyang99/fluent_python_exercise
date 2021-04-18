b = 6
def f1(a):
    print(f"{a=}")
    print(f"{b=}")
    print(f"func f() {locals()}")
    b = 15

f1(5)