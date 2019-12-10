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


def balanced_para(exp):
    stack = Stack()
    for elem in exp:
        if elem == '(':
            stack.push(elem)
        elif elem == ')':
            stack.pop()
        else:
            continue
    if stack.is_empty():
        return True
    return False
