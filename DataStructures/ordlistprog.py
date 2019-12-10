from orderedlist import Node, OrderedList

def modfile(file, user_num):
    ret_str = ''
    f = open(file, 'r')
    for line in f:
        if ',' in line:
            num_arr = line.split(',')
        else:
            num_arr = line.split()
    num_arr = [int(num) for num in num_arr]
    print(num_arr)
    f.close()
    li = OrderedList()
    for num in num_arr:
        li.add(num)
    li.display()
    if li.search(user_num) is True:
        x = li.index(user_num)
        li.pop(x)
    else:
        li.add(user_num)
    f = open(file, 'r+')
    for num in li:
        ret_str = ret_str + ' ' + str(num)
    f.write(ret_str)
    f.close()
