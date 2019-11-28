def userInput():

    x = int(input("Please Enter X co-ordinates :\n"))
    y = int(input("Please Enter Y co-ordinates :\n"))

    return x,y

def distance(x,y):
    return (x**2 + y**2)**0.5
