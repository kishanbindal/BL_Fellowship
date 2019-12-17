"""
    @Summary driver code for deckQ.py, Adding cards to player using linked list and Queue

    @Author Kishan Bindal

    @Since December 2019
"""
from oop import deckQ
from oop import utility


def deck_drive():

    deck = deckQ.Deck()
    players = utility.Queue()  # Initialize Queue for players playing
    print("Options :")
    print("1. Show Deck\n2. Shuffle Deck\n3. Deal 9 Cards to 4 players\n4. Show Player cards\n5. Exit\n")
    while True:
        while True:  # Take User Input
            try:
                user_choice = int(input("Enter choice (1-5) : "))
            except ValueError:
                print("Please Enter Integer Values from 1 to 5 only!")
            else:
                break
        if user_choice == 1:
            deck.show()  # Show cards in deck
        elif user_choice == 2:
            deck.shuffle()  # Shuffle cards in deck
        elif user_choice == 3:
            for i in range(4):
                player = deckQ.Player()  # Create player
                for j in range(9):
                    player.add_card_to_hand(deck.deal())  # Add to linked list in player.hand
                    player.add_to_queue()  # adding cards from linked list to Queue
                players.enqueue(player)  # adding single players to Queue of multiple players
        elif user_choice == 4:
            count = 1
            while players.size() != 0:
                print(f"-----PLayer {count}'s cards--------")
                x = players.deque()  # Extract player from queue
                while x.q.is_empty() is False:
                    print(x.q.deque())  # Extract player card fro player's card Queue
                count += 1
        else:
            break


if __name__ == '__main__':
    deck_drive()
