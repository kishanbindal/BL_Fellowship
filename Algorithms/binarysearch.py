f = open('Binarysearchlist.txt','w+')
for i in range(1):
    f.write("This,is,a,sentence,in,file,binarysearchlist.txt")
f.close()
list_of_words = []
with open('D:\Bridgelabz\Algorithms\Binarysearchlist.txt','r') as f:
    for line in f:
        list_of_words = line.split(',')

def binarySearch(lst):
    check_word = input("Please enter the word you would like to check for in the file :\n")
    if check_word in list_of_words:
        return True
    return False

list_of_words = sorted(list_of_words)
print(list_of_words)

def binarySearchAlgo(lst,start,stop,word):

    if stop >= start:
        mid = (start + (stop - start) + 1) // 2
        if lst[mid] == word:
            return mid

        elif lst[mid] > word:
            return binarySearchAlgo(lst,start,mid-1,word)

        else:
            return binarySearchAlgo(lst,mid+1,stop,word)
    else:
        return -1

print(binarySearchAlgo(list_of_words,0,len(list_of_words)-1,'binaryseachlist.txt'))