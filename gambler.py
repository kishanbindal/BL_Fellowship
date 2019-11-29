import random

def takeUserInput():

    stake = int(input("Enter starting Stake/Amount :\n"))
    goal = int(input("Enter Goal :\n"))
    trial = int(input("Enter number of trials :\n"))
    return stake,goal,trial

def gamble(stake,goal,trials):
    bets = 0
    wins = 0
    for i in range(0,trials):
        chips = stake
        while (chips > 0 and chips < goal):
            bets += 1
            if random.uniform(0,1) > 0.5:
                chips += 1
            else:
                chips  -= 1
        if chips == goal:
            wins +=1
    print(f"{wins} wins from {trials}")
    print(f"Percent of games won : {(wins/trials)*100}")
    print(f"Average number of bets : {bets/trials}")

stake,goal,trial = takeUserInput()
gamble(stake,goal,trial)