def takeNum():
    while True:
        try:
            x = int(input("Please Enter Integer Value Between 0 and 31 : \n"))
            if x < 0 or x > 31:
                raise ValueError
        except ValueError:
            print("Please Enter only int() Values between 0 and 31!!")
        else:
            return x

def powerOf2(num):
    result = []
    for i in range(0,num+1):
        result.append(2**i)
        print(f"2 to the power of {i} -----> {result[i]}")
    return result
