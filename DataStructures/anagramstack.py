from DataStructures import utility
from DataStructures import primeanagram


def prime_stack(lst):
    """lst should be a 2D array"""
    temp = lst[0]
    linked_list = utility.List()
    stk = utility.Stack()
    for num in temp:  # Adding elements into the linked list
        linked_list.append(num)
    while linked_list.isEmpty() is False:  # As long as linked list is not empty keep adding values into stack
        stk.push(linked_list.pop(0))  # pop(0) since we want to print anagrams in reverse order
    while stk.size() != 0:  # As long as stack is not empty keep popping values to print
        print(stk.pop())


if __name__ == "__main__":
    x = primeanagram.primerange2d.check_prime_range()
    y = primeanagram.check_prime_anagram(x)
    prime_stack(y)
