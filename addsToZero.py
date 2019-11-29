def takeInput():
    x = int(input("Please Enter number of numbers you would like to test : \n"))
    numbers_array = []
    for i in range(0,x):
        numbers_array.append(int(input(f"Please Enter {i+1} Number  :\n")))
    return numbers_array


def addsToZero(array):
    number_of_triplets = 0
    for i in range(len(array)-2):
        for j in range(i+1,len(array)-1):
            for k in range(j+1,len(array)):
                if array[i] + array[j] + array[k] == 0:
                    number_of_triplets += 1
                    print(f"{array[i]} + {array[j]} + {array[k]} = 0")
    print(number_of_triplets)
    return number_of_triplets


