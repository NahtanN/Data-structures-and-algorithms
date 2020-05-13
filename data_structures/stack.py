from data_structures.doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.stack = DoublyLinkedList()

    def push(self, data):
        self.stack.add_node(data)

    @property
    def pop(self):
        self.stack.remove_node()

    @property
    def empty(self):
        self.stack.lenght = 0

    @property
    def peek(self):
        return self.stack.show(reverse=True)
