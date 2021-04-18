from vector2d_v3 import Vector2d

class ShortVector2d(Vector2d):
    typecode = 'f'

if __name__ == '__main__':
    sv = ShortVector2d(1/11, 1/27)

    print(f"{sv=}")
    print(f"{len(bytes(sv))=}")