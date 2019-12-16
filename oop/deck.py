import random


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    suits = ['Diamond', 'Club', 'Spade', 'Heart']
    ranks = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
             'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        n = int(input("Enter number of times you would like to shuffle the deck"))
        for i in range(n):
            random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


if __name__ == '__main__':
