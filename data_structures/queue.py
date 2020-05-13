from data_structures.doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def add(self, data):
        self.queue.add_node(data)

    @property
    def remove(self):
        self.queue.remove_node(1)

    @property
    def empty(self):
        self.queue.lenght = 0

    @property
    def peek(self):
        self.queue.show()

