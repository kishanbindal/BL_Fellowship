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
    f.close()
    li = OrderedList()
    for num in num_arr:
        li.add(num)
    if li.search(user_num) is True:
        li.remove(user_num)
    else:
        li.add(user_num)
    f = open(file, 'w')
    for num in li:
        ret_str = ret_str + ' ' + str(num)
    print(ret_str)
    f.write(ret_str)
    f.close()