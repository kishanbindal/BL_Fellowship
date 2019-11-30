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

def binarySearchAlgo(lst,start,stop,word):
    pass


print(binarySearch(list_of_words))
