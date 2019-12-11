from DataStructures import hashtable as ht


def take_input():
    user_inp = int(input("Please Enter Number : \n"))
    return user_inp


def check_ht(user_num):

    x = ht.hash_table('num_file_hash')  # hashtable stored in variable x
    x_idx = ht.hash_function(user_num)

    for i in range(len(x)):
        if x_idx == i:  # if index = hash index open linked list at that index
            link_list = x[i]
            if link_list.search(user_num) is True:  # check if user_num in LL, if True->remove ,else->add
                link_list.remove(user_num)
            else:
                link_list.add(user_num)
    for ele in x:
        ele.display()
    return x
