class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.__head = None
        self.__lenght = 0

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, new_head):
        self.__head = new_head

    @property
    def lenght(self):
        return self.__lenght

    @lenght.setter
    def lenght(self, new_lenght):
        self.__lenght = new_lenght

    # PRIVATE METHODS ---------------------------------------------------------------------------------

    def _create_node(self, node):
        return Node(node)

    def _len_linked_list(self):
        pass

    def _find_node(self, position):


    def _insert_node(self, node, position=None):
        node = self._create_node(node)

        # Create a new doubly linked list
        if self.head is None:
            self.head = node
            return True

        # Insert at the end of DoublyLinkedList
        if position is None:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            node.prev = current_node
            current_node.next = node
            return True

        # Insert at a given position
        if position not in [None]:
            self._find_node(position)

        # Insert at the head of the DoublyLinkedList
        temporary = self.head
        temporary.prev = node
        node.next = temporary
        self.head = node
        del temporary
        return True

    # PUBLIC METHODS ----------------------------------------------------------------------------------

    def add_node(self, node, position=None):
        validation = self._insert_node(node, position)

        if validation is True:
            self._len_linked_list()
            return
        raise IndexError("Position out of range")

    def show(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
