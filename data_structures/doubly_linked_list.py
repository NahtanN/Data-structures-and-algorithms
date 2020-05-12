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
        size = self.lenght / 2

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
        if position is not None:
            if position > self.lenght + 1 or position <= 0:
                return False

        node = self._create_node(node)

        # Create a new doubly linked list
        if self.head is None:
            self.head = node
            return True

        # Insert at the end of DoublyLinkedList
        if position in [None, self.lenght + 1]:
            self.final = node
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            node.prev = current_node
            current_node.next = node
            return True

        # Insert at a given position
        if position not in [None, 1]:
            current_node = self._find_node(position)
            current_node.prev.next = node
            node.prev = current_node.prev
            node.next = current_node
            current_node.prev = node
            return True

        # Insert at the head of the DoublyLinkedList
        self.head.prev = node
        node.next = self.head
        self.head = node
        return True

    def _delete_node(self, position=None):
        if position is not None:
            if position > self.lenght or position < 0:
                return False

        # Delete the last Node
        if self.lenght == 1:
            self.head = None
            self.final = None
            print("\033[34mThe list has been emptied\033[30m")
            return True

        # Delete the final Node
        if position in [None, self.lenght]:
            self.final = self.final.prev
            self.final.next = None
            return True

            # Delete Node of a given position
        if position not in [None, 1]:
            current_node = self._find_node(position)
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            del current_node
            return True

        # Delete the head Node
        self.head = self.head.next
        self.head.prev = None
        return True

    # PUBLIC METHODS ----------------------------------------------------------------------------------

    def add_node(self, node, position=None):
        validation = self._insert_node(node, position)

        if validation is True:
            self._len_linked_list()
            return
        print("\033[31mPosition out of range\033[30m")

    def delete_node(self, position=None):
        validation = self._delete_node(position)

        if validation is True:
            self.lenght -= 1
            return
        print("\033[31mPosition out of range\033[30m")

    def show(self):
        if self.lenght != 0:
            current_node = self.head
            pos = 1
            while current_node is not None:
                print(f"\033[33m[{pos}]\033[30m{current_node.data}")
                current_node = current_node.next
                pos += 1
            return
        print("\033[34mThe list is empty.\033[30m")
