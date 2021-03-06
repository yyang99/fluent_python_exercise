b = 6
def f1(a):
    print(f"{a=}")
    print(f"{b=}")
    print(f"func f() {locals()}")

f1(5)