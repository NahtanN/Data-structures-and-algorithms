class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.__head = None
        self.__final = None
        self.__lenght = 0

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, new_head):
        self.__head = new_head

    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, new_final):
        self.__final = new_final

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
        current_node = self.head
        cont = 0
        while True:
            cont += 1
            if current_node.next is None:
                self.lenght = cont
                return
            current_node = current_node.next

    def _find_node(self, position):
        size = self.lenght/2

        if position < size + 1:
            current_node = self.head
            pos = 0
            while True:
                pos += 1
                if pos == position:
                    return current_node
                current_node = current_node.next

        current_node = self.final
        pos = self.lenght + 1
        while True:
            pos -= 1
            if pos == position:
                return current_node
            current_node = current_node.prev

    def _insert_node(self, node, position=None):
        node = self._create_node(node)

        # Create a new doubly linked list
        if self.head is None:
            self.head = node
            return True

        # Insert at the end of DoublyLinkedList
        if position in [None, self.lenght + 1]:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            self.final = node
            node.prev = current_node
            current_node.next = node
            return True

        # Insert at a given position
        if position not in [None, 0, 1]:
            current_node = self._find_node(position)
            temporary = current_node.prev
            temporary.next = node
            node.prev = temporary
            node.next = current_node
            current_node.prev = node
            del temporary
            return True

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
        pos = 1
        while current_node is not None:
            print(f"\033[33m[{pos}]\033[30m{current_node.data}")
            current_node = current_node.next
            pos += 1
