# docktest: +ELLIPSIS
import collections
import random

Card = collections.namedtuple('Card', ('rank', 'suit'))

# def card_to_str(card: Card):
#     return "{} of {}".format(card.rank, card.suit)
#
# Card.__str__ = card_to_str

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('AJQK')
    suits = "spades diamonds hearts clubs".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in FrenchDeck.suits for rank in FrenchDeck.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == "__main__":
    deck = FrenchDeck()
    print(f"len(cards)={len(deck)}")
    position = 31
    print(f"cards {position} = {deck[position]}")
    print("*** whole deck ***")

    def card_to_str(card: Card):
        return "{} of {}".format(card.rank, card.suit)

    Card.__str__ = card_to_str

    for i in deck:
        print(i)
    print("******************")
    print(f"random draw {random.choice(deck)}")
    # print("*** shuffle deck ***")
    # random.shuffle(cards)
    # for i in cards:
    #     print(i)
    # print("******************")
    print("*** sorted deck - rank first ***")
    suit_values = dict(spades=3, diamonds=2, hearts=1, clubs=0)
    def spades_high_ordering(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    for card in sorted(deck, key=spades_high_ordering):
        print(card)
    print("******************")
    print("*** sorted deck - suit first ***")
    suit_values = dict(spades=3, diamonds=2, hearts=1, clubs=0)
    def spades_high_ordering_suit_first(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return suit_values[card.suit] * len(FrenchDeck.ranks) + rank_value

    for card in sorted(deck, key=spades_high_ordering_suit_first):
        print(card)
    print("******************")
    print("*** shuffle deck ***")
    def setcard(deck, index, card):
        deck._cards[index] = card

    FrenchDeck.__setitem__ = setcard

    random.shuffle(deck)
    for i in deck:
        print(i)
    print("******************")