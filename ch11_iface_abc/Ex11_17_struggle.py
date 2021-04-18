class Struggle:
    pass
    def __len__(self):
        return 23


from mycollections import MySized

if __name__ == '__main__':
    print(f"{issubclass(Struggle, MySized)=}")
    print(f"{isinstance(Struggle(), MySized)=}")


