from DataStructures import unorderedlist


def checkfile(file, user_word):
    # Open A file and read it's contents into a list
    f = open(file, 'r+')
    unordered_list = unorderedlist.List()
    ret_str = ''
    word_arr = []
    for line in f:
        word_arr = line.split()
    f.close()
    # Words from the list are added into the linked list
    for word in word_arr:
        unordered_list.append(word)
    # search for  the word and check if the word is in the list. If True, Remove the word else add the word
    x = unordered_list.search(user_word)
    if x is True:
        unordered_list.remove(user_word)
    else:
        unordered_list.append(user_word)
    # Adding the words back into the file.
    for w in unordered_list:
        ret_str = ret_str + ' ' + w
    f = open(file, 'w')
    f.write(ret_str)
    f.close()
