import random


def player_marker():

    while True:
        play_marker = input("Please choose 'X' or 'O' :\n")
        comp_marker = ''
        if play_marker.upper() == 'X':
            comp_marker = 'O'
            print(f"Player : {play_marker}\nComputer : {comp_marker}")
            return [play_marker.upper(),comp_marker]
        elif play_marker.upper() == 'O':
            comp_marker = 'X'
            print(f"Player : {play_marker}\nComputer : {comp_marker}")
            return [play_marker.upper(), comp_marker]
        else:
            print("Please choose 'X' or 'O' only!")


def display_board(board):
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("---------------")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---------------")
    print(f" {board[1]} | {board[2]} | {board[3]} ")


def choose_position():
    while True:
        position = int(input("Please Enter position between 1-9 :\n"))
        if position in range(1,10):
            break
        else:
            print("Please enter Valid position")
    return position


def place_marker_player(player_marker,board):
    while True:
        pos = choose_position()
        if board[pos] == ' ':
            board[pos] = player_marker
            break
        else:
            print("Enter Position which is not taken")
            continue


def place_marker_computer(marker,board):
    while True:
        pos = comp_position()
        if board[pos] == ' ':
            board[pos] = marker
            break


def comp_position():
    comp_position = random.randint(1,9)
    return comp_position


def check_win(marker,board):
    #Check rows
    if (board[1]==board[2]==board[3] == marker) or (board[4]==board[5]==board[6]==marker) or (board[7] == board[8]==board[9] == marker):
        return True
    # Check columns
    elif (board[1]==board[4]==board[7] == marker) or (board[2]==board[5]==board[8]==marker) or (board[3] == board[6]==board[9] == marker):
        return True
    #Check Diagonals
    elif (board[1]==board[5]==board[9] == marker) or (board[3]==board[5]==board[7]==marker):
        return True
    return False


def full_board_check(board):
    if ' ' in board:
        return False
    return True

global playing
playing = True


while playing:
    print("Welcome to Tic Tac Toe!! \n")
    print("Player chooses marker\n")
    board = [0,' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player_marker,computer_marker = player_marker()
    x = random.randint(0, 1)
    if x == 1:
        print(f"Player '{player_marker}' goes first\nComputer '{computer_marker}' will go second")
        while True:
            display_board(board)
            print("Player's Turn\n")
            place_marker_player(player_marker,board)
            if check_win(player_marker,board):
                print("Player has won!!!!")
                break
            elif full_board_check(board):
                print("Game is a Tie!")
                break
            display_board(board)
            print("Computer's Turn\n")
            place_marker_computer(computer_marker,board)
            if check_win(computer_marker,board):
                print("Computer has Won!")
                break
            elif full_board_check(board):
                print("Game is a Tie!")
                break
    else:
        print(f"Computer '{computer_marker}' goes first\nPlayer '{player_marker}' will go second")
        while True:
            display_board(board)
            print("Computer's Turn\n")
            place_marker_computer(computer_marker,board)
            if check_win(computer_marker,board):
                print("Computer has won!!!!")
                break
            elif full_board_check(board):
                print("Game is a Tie!")
                break
            display_board(board)
            print("Player's Turn\n")
            place_marker_player(player_marker,board)
            if check_win(player_marker,board):
                print("Player has Won!")
                break
            elif full_board_check(board):
                print("Game is a Tie!")
                break

    display_board(board)
    replay = input("\n\nWould you like to play again?? 'Y' or 'N' \n")
    if replay[0].upper() == 'Y':
        continue
    else:
        print("Thank you for playing.")
        playing = False


