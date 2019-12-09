

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class OrderedList:

    def __int__(self):
        self.head = None

    def add(self, item):
        cur_node = self.head
        previous_node = None
        while cur_node != None:
            if cur_node.data < item:
                break
            
