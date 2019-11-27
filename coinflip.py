import random

def userInput():
    x = int(input("Please Enter number of times you would like to flip coin : \n"))
    if x < 1:
        raise ValueError(" Only nonzero Poistive Values can Be passed")
    return x


def flipCoin(n):
    head_count = 0
    tail_count = 0
    for i in range(n):
        x = random.randint(0,1)
        if x == 1:
            head_count +=1
        elif x == 0:
            tail_count += 1
    print(f"Percentage Head Count : {head_count/(head_count+tail_count)}")


