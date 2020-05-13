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
        """Create a new Node"""
        return Node(node)

    def _find_node(self, position):
        """
        Find the requested Node
        :return: current_node
        """
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
        """
        Inserts the Node in the requested position
        :param node: any data or object
        :param position: None by default
        :return: None
        """

        node = self._create_node(node)

        # Create a new doubly linked list
        if self.head is None:
            self.head = node
            return

        # Insert at the end of DoublyLinkedList
        if position in [None, self.lenght + 1]:
            self.final = node
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            node.prev = current_node
            current_node.next = node
            return

        # Insert at a given position
        if position not in [None, 1]:
            current_node = self._find_node(position)
            current_node.prev.next = node
            node.prev = current_node.prev
            node.next = current_node
            current_node.prev = node
            return

        # Insert at the head of the DoublyLinkedList
        self.head.prev = node
        node.next = self.head
        self.head = node
        return

    def _delete_node(self, position=None):
        """
        Delete the Node of a requested position
        :param position: None by default
        :return: None
        """

        # Delete the last Node
        if self.lenght == 1:
            self.head = None
            self.final = None
            return print("\033[34mThe list has been emptied\033[30m")

        # Delete the final Node
        if position in [None, self.lenght]:
            self.final = self.final.prev
            self.final.next = None
            return

        # Delete Node of a given position
        if position not in [None, 1]:
            current_node = self._find_node(position)
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            del current_node
            return

        # Delete the head Node
        self.head = self.head.next
        self.head.prev = None
        return

    def _pick_up(self, position=None):
        """
        :param position: None
        :return: Any Node of the DoublyLinkedList
        """

        # Pick the final Node
        if position is None or position == self.lenght:
            return self.final.data

        # Pick the head Node
        if position == 1:
            return self.head.data

        # Pick the node of a given position
        return self._find_node(position).data

    # PUBLIC METHODS ----------------------------------------------------------------------------------

    def add_node(self, node, position=None):
        """
        Public method to add a Node to DoublyLinkedList
        :param node: any data or object
        :param position: None by default
        :return: print statement, if the position is out of range
        """

        if position is not None:
            if position > self.lenght + 1 or position <= 0:
                return print("\033[31mPosition out of range\033[30m")

        self._insert_node(node, position)
        self.lenght += 1

    def remove_node(self, position=None):
        """
        Public method to delete a Node to DoublyLinkedList
        :param position: None by default
        :return: print statement, if the position is empty or out of range
        """

        if self.lenght == 0:
            return print("\033[34mThe list is empty\033[30m")

        if position is not None:
            if position > self.lenght or position <= 0:
                return print("\033[31mPosition out of range\033[30m")

        self._delete_node(position)
        self.lenght -= 1

    def get_node(self, position=None):
        """
        :param position: None by default
        :return: Any Node of the DoublyLinkedList
        """
        if self.lenght == 0:
            return print("\033[34mThe list is empty\033[30m")

        if position is not None:
            if position > self.lenght or position <= 0:
                return print("\033[31mPosition out of range\033[30m")

        return self._pick_up(position)

    def show(self, reverse=False):
        """
        Public method to print the DoublyLinkedList
        :param reverse: False by default. If its True, reverse the print statement
        :return: None
        """

        if self.lenght != 0:
            if reverse is False:
                current_node = self.head
                pos = 1
                while current_node is not None:
                    print(f"\033[33m[{pos}]\033[30m{current_node.data}")
                    current_node = current_node.next
                    pos += 1
                return

            if reverse is True:
                current_node = self.final
                pos = self.lenght
                while current_node is not None:
                    print(f"\033[33m[{pos}]\033[30m{current_node.data}")
                    current_node = current_node.prev
                    pos -= 1
                return

        print("\033[34mThe list is empty.\033[30m")

