from DataStructures import utility


# takes in an item and returns it's index position in the slot
def hash_function(item):
    return item % 11


def hash_table(file):

    buckets = 11  # Number of slots in the hash table
    table = [] * buckets  # Initializing the slots to have empty value
    num_arr = []

    f = open(file, 'r')

    for line in f:  # Read the numbers in the file into a List/Array
        num_arr = line.split()

    num_arr = [int(x) for x in num_arr]  # Convert values to int data type

    for i in range(buckets):  # Creating linked list objects at each bucket/slot in the hash table
        table.append(utility.OrderedList())

    for num in num_arr:
        idx = hash_function(num)  # Generating index position for the hash table
        ret_ll = table[idx]  # Retrieving linked list object stored in particular index position
        ret_ll.add(num)  # Adds the number to the linked list
        #ret_ll.display()

    return table
