# =======================================================================================================
# Unordered Linked List


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class List:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        # if head is  None, it means the list is empty, as otherwise self.head with a single element
        # will be an instance of the Node Class.
        return self.head is None

    def add(self, item):
        new_node = Node(item)
        # linking new node to existing node(which is stored in self.head = nextNode in network)
        new_node.next = self.head
        # making the current_node(new_node) the head.
        self.head = new_node

    def remove(self, item):
        cur_node = self.head
        previous = None
        # Traverse through the list
        while cur_node.data != item:
            previous = cur_node
            cur_node = cur_node.next
        print(f"Removing {item} from Linkedlist.")
        if previous is None:
            self.head = cur_node.next
        else:
            previous.next = cur_node.next

    def search(self, item):
        cur_node = self.head
        while True:
            if cur_node.data == item:
                return True
            elif cur_node.next is None:
                if cur_node.data == item:
                    return True
                return False
            else:
                cur_node = cur_node.next

    def size(self):
        if self.isEmpty() is True:
            return 0
        total = 1
        cur_node = self.head
        while cur_node.next is not None:
            total += 1
            cur_node = cur_node.next
        return total

    def append(self, item):
        cur_node = self.head
        if cur_node is None:
            self.add(item)
        else:
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = Node(item)

    def index(self, item):
        count = 0
        cur_node = self.head
        while cur_node.next is not None:
            if cur_node.data == item:
                return count
            cur_node = cur_node.next
            count += 1
        if cur_node.next is None and cur_node.data == item:
            return count
        return False

    def insert(self, pos, item):
        index = 0
        previous_node = None
        cur_node = self.head
        if pos == 0:
            self.add(item)
        while cur_node.next is not None:
            previous_node = cur_node
            cur_node = cur_node.next
            index += 1
            if pos == index:
                add_node = Node(item)
                previous_node.next = add_node
                add_node.next = cur_node

    def pop(self):
        cur_node = self.head
        count = 0
        previous = None
        while cur_node.next is not None:
            previous = cur_node
            cur_node = cur_node.next
            count += 1
        previous.next = None
        return cur_node.data

    def pop(self, pos):
        cur_node = self.head
        index = 0
        previous_node = None
        if pos > self.size() - 1:
            raise IndexError("Linked List Index Out of Range")
        if pos == 0:
            previous_node = cur_node
            cur_node = cur_node.next
            self.head = cur_node
            return previous_node.data
        while cur_node.next is not None:
            previous_node = cur_node
            cur_node = cur_node.next
            index += 1
            if index == pos:
                print(index)
                previous_node.next = cur_node.next
                return cur_node.data

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            elems.append(cur_node.data)
            cur_node = cur_node.next
        if cur_node.next is None:
            elems.append(cur_node.data)
        print(elems)

    def __iter__(self):
        cur_node = self.head
        while cur_node.next is not None:
            yield cur_node.data
            cur_node = cur_node.next
        if cur_node.next is None:
            yield cur_node.data

# =================================================================================================================================
# Ordered Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class OrderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        cur_node = self.head
        previous_node = None
        new_node = Node(item)
        # Traversing through the Nodes and breaking out when current node
        # data becomes larger
        while cur_node is not None:
            if cur_node.data > item:
                break
            previous_node, cur_node = cur_node, cur_node.next
        # for first node , when linked list is empty
        if previous_node is None:
            new_node.next, self.head = self.head, new_node
        # Adding nodes in between
        else:
            previous_node.next, new_node.next = new_node, cur_node

    def remove(self, item):
        cur_node = self.head
        previous_node = None
        while cur_node.data != item:
            previous_node = cur_node
            cur_node = cur_node.next
        print(f"Removing {item} from the Linked List")
        if previous_node is None:
            self.head = cur_node.next
        else:
            previous_node.next = cur_node.next

    # searches the linked list for input item and returns True or False
    def search(self, item):
        cur_node = self.head
        while True:

            if cur_node is None:
                return False
            # checking for the item in the node
            elif cur_node.data == item:
                return True
            # Traversing through the linked list
            else:
                cur_node = cur_node.next

    # Return Boolean based on whether the list is empty or not
    def is_empty(self):
        return self.head is None

    # Is called on the linked list and returns the Number of elements in linked list
    def size(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count

    # Display's the items in the linked List as a list() data type
    def display(self):
        elems = []
        cur_node = self.head
        if self.size() == 0:
            return elems
        while cur_node.next is not None:
            elems.append(cur_node.data)
            cur_node = cur_node.next
        elems.append(cur_node.data)
        print(elems)

    # Takes in user input and return the index position of the item
    def index(self, item):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            if cur_node.data == item:
                return count
            cur_node = cur_node.next
            count += 1

    # Method called on the linked List which returns the last value of the list and removes it from Linked List
    def pop(self):
        cur_node = self.head
        previous_node = None
        if self.size() == 1:
            pop = cur_node.data
            self.head, cur_node = None, self.head
            return pop
        while cur_node.next is not None:
            previous_node, cur_node = cur_node, cur_node.next
        previous_node.next = None
        return cur_node.data

    # Method called on the Linked List which returns Value at the specified index and removes it from Linked List
    def pop(self, pos):
        cur_node = self.head
        previous_node = None
        count = 0
        if pos > self.size()-1:
            raise IndexError("Linked List Index Out of Range")
        while cur_node.next is not None:
            if pos == 0:
                previous_node, cur_node = cur_node, cur_node.next
                self.head = cur_node
                return previous_node.data
            else:
                previous_node, cur_node = cur_node, cur_node.next
                count += 1
                if pos == count:
                    previous_node.next = cur_node.next
                    return cur_node.data

    def __iter__(self):
        cur_node = self.head
        while cur_node is not None:
            yield cur_node.data
            cur_node = cur_node.next

# =======================================================================================================================
# Stack


class Stack:

    # Initialize a Stack to hold the values
    def __init__(self):
        self.data = []

    # Adds 'item' to the top of the stack. Returns nothing.
    def push(self, item):
        self.data.append(item)

    # Removes the top most element in the Stack
    def pop(self):
        return self.data.pop()

    # Returns the top most element in the Stack
    def peek(self):
        return self.data[-1]

    # Returns true if stack is empty, False otherwise
    def is_empty(self):
        return len(self.data) == 0

    # Returns the number of elements stored in the stack
    def size(self):
        return len(self.data)

# ======================================================================================================================
# Queue


class Queue:

    def __init__(self):
        self.data = []

    # Insert item at the back of the queue (left most of the list)
    def enqueue(self, item):
        self.data.insert(0, item)

    # Remove item from the front of the queue (Right most element)
    def deque(self):
        return self.data.pop()

    # Check if the Queue is empty, return True if empty
    def is_empty(self):
        return len(self.data) == 0

    # return the number of elements in the Queue
    def size(self):
        return len(self.data)

# ======================================================================================================================
# Deque


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
