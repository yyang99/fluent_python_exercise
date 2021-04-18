b = 6
def f1(a):
    global b
    print(f"{a=}")
    print(f"{b=}")
    print(f"func f() {locals()}")
    b = 9

f1(5)
print(f"main: {b= }")