import math


class Node:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, cur_node):
        if val < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(val)
            else:
                self._insert(val, cur_node)
        else:
            if cur_node.right_child is None:
                cur_node.right_child = Node(val)
            else:
                self._insert(val, cur_node)

    def in_order(self):
        if self.root is not None:
            self._in_order(self.root)

    def _in_order(self, current_node):
        if current_node is not None:
            self._in_order(current_node.left_child)
            print(current_node.value)
            self._in_order(current_node.right_child)

    def count_binary(self, n):
        return (math.factorial(2*n))/(math.factorial(n+1)*math.factorial(n))


if __name__ == "__main__":
    bst = BinarySearchTree()
    for i in range(1, 7):
        print(bst.count_binary(i))
