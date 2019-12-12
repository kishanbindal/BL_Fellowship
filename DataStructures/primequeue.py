from DataStructures import utility
from DataStructures import primeanagram


def prime_queue(lst):
    """Lst Should be 2-D Array"""
    temp = lst[0]  # Taking only anagrams from primeanagram.py
    linked_list = utility.List()
    qu = utility.Queue()
    for num in temp:
        linked_list.append(num)  # Adding anagrams from temp to linked list
    while linked_list.isEmpty() is False:
        qu.enqueue(linked_list.pop(0))  # Adding prime anagrams from linked lis tto Queue
    while qu.is_empty() is False:
        print(qu.dequeue())  # Printing the anagrams from Queue until Queue become empty and nothing to print


if __name__ == "__main__":
    x = primeanagram.primerange2d.check_prime_range()
    y = primeanagram.check_prime_anagram(x)
    prime_queue(y)
