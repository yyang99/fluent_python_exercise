from vector2d_v3 import Vector2d

v1 = Vector2d(1.1, 2.2)

dumpd = bytes(v1)
print(f"{dumpd=}")

print (f"{len(dumpd)=}")

v1.typecode = 'f'

dumpf = bytes(v1)

print(f"{dumpf=}")

print (f"{len(dumpf)=}")