"""
    @ Summary Driver code for DeckOfCards

    @Author Kishan Bindal

    @Since December 2019
"""
from oop import deck


def deck_run():  # Function to display options to user

    d = deck.Deck()  # Build a deck
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
            d.show()  # Show cards in deck
        elif user_choice == 2:
            d.shuffle()  # Shuffle cards in deck
        elif user_choice == 3:
            x = d.deal_to_players()  # Deal 9 cards to 4 players
        elif user_choice == 4:
            count = 1
            for player in x:
                print(f"-----------Player{count}'s Cards-----------")
                for card in player:  # Display cards of each of the 4 players
                    print(card)
                count += 1
        else:
            break


# Driver Code
if __name__ == '__main__':
    deck_run()
