charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(f"{lewis is charles=}")
print(f"{id(charles)=}, {id(lewis)=}")

alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(f"{alex == charles=}")
print(f"{alex is not charles=}")