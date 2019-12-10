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
