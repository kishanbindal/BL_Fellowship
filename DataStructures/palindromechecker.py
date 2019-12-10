class Deque:

    def __init__(self):
        self.data = []

    # Function to add element to the front of Deque
    def add_front(self, item):
        self.data.append(item)

    # Function to add element to the rear of the Deque
    def add_rear(self, item):
        self.data.insert(0, item)

    # Function to remove element at the front of the Deque, returns the removed element
    def remove_front(self):
        return self.data.pop()

    # Function to remove element at the end(last element) of the Deque, returns removed element
    def remove_rear(self):
        return self.data.pop(0)

    # Function to check if the Deque object has any elements, returns True if empty
    def is_empty(self):
        return len(self.data) == 0

    # Function to find the number of elements in the Deque object
    def size(self):
        return len(self.data)


# Function to take input string from user and returns it.
def take_input():
    return input("Please Enter the string that you would like to check for Palindrome :\n")


def check_palindrome(user_string_input):
    d = Deque()  # Create a Deque object
    for letter in user_string_input:
        d.add_rear(letter.lower())  # Add characters from the string to the Deque
    while d.size() > 1:  # in case off no. of characters or single character

        # if the element being removed(right and left) are unequal then they aren't Palindrome
        if d.remove_front() != d.remove_rear():
            return False

    return True
