import collections
Card = collections.namedtuple('Card', ('rank', 'suit'))

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('AJQK')
    suits = "spades diamonds hearts clubs".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in FrenchDeck.ranks for suit in FrenchDeck.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == "__main__":
    cards = FrenchDeck()
    print(f"len(cards)={len(cards)}")
    position = 31
    print(f"cards {position} = {cards[position]}")
    for i in cards:
        print(i)