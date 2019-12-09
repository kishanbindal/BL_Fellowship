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
        if previous == None:
            self.head = cur_node.next
        else:
            previous.next = cur_node.next

    def search(self, item):
        cur_node = self.head
        while True:
            if cur_node.data == item:
                return True
            elif cur_node.next == None:
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
        while cur_node.next != None:
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
