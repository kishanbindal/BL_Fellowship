"""
    @Summary Creating players, adding their cards in queue and adding these players to player Queue

    @Author Kishan Bindal

    @since December 2019
"""
from oop import utility
import random


class Card:  # Card class to build card object have suit and rank

    values = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):  # To print the card using print()
        return f"{self.rank} of {self.suit}"


class Deck:  # To build deck of cards, shuffle deck and deal to players
    # Class variables suits and ranks as they do not change for instance of deck
    suits = ['Diamond', 'Club', 'Spade', 'Heart']
    ranks = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
             'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):  # Initialise deck into list and add Card objects to deck
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):  # Shuffle deck using random.shuffle
        n = int(input("Enter number of times you would like to shuffle the deck"))
        for i in range(n):
            random.shuffle(self.deck)

    def deal(self):  # Function to deal card, returns the card
        return self.deck.pop()

    def show(self):  # Function to show contents of the deck
        for card in self.deck:
            print(card)

    def deal_to_players(self):  # Function to deal 9 cards to 4 players and return it in a 2-D Array
        players = []
        for i in range(4):
            player = []
            for j in range(9):
                player.append(self.deal())
            players.append(player)
        return players


class Player:  # Added Player class

    def __init__(self):
        self.hand = utility.OrderedList()  # Hand attribute to add card values to Queue
        self.q = utility.Queue()  # q attribute to add card from linked list to Queue

    def add_card_to_hand(self, card):  # adding cards to linked list by card value
        self.hand.add(card.values[card.rank])

    def add_to_queue(self):  # Adding cards from linked list to Queue
        self.q.enqueue(self.hand.pop(0))

    def show_hand(self):  # Removing cards from Queue to show their content
        print(self.q.deque())
