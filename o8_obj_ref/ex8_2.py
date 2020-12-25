class Gizmo:
    def __init__(self):
        print('Gizmo id: {}'.format(id(self)))

x = Gizmo()

# y = Gizmo() * 10

print(dir())