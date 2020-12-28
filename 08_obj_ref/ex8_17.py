import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
print(f"{wref=}")
print(f"{wref()=}")

