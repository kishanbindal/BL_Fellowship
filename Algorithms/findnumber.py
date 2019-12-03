def userInput():
    inp = int(input("Enter upper range for finding your number : \n"))
    return list(range(inp))

def binary(arr,start,stop,value):

    if stop > start:

        mid = (start + stop)// 2
        print(mid)

        if arr[mid] == value:
            print(f"Number : {arr[mid]}\nIndex : {mid}")
            return mid

        x = input(f"Is the number in range {start+1} and {mid+1}? True/False?")

        if x.lower() == 'true':
            return binary(arr,start,mid, value)
        else:
            return binary(arr,mid+1,stop,value)
    return -1

arr = userInput()
print(arr)
print(binary(arr,0,len(arr)-1,21))
