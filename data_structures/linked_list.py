class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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

    # PRIVATE METHODS -------------------------------------------------------------------------------------

    # This function create a new node
    def _create_node(self, new_node):
        return Node(new_node)

    # This function find the postion of a requested node
    def _find_position(self, position):
        current_node = self.head
        previous_node = None

        pos = 0
        while True:
            if pos == position - 1:
                return current_node, previous_node
            previous_node = current_node
            current_node = current_node.next
            pos += 1

    def _len_linked_list(self):
        current_node = self.head

        count = 0
        while True:
            count += 1
            if current_node.next is None:
                self.lenght = count
                return
            current_node = current_node.next

    def _insert_node(self, node, position=None):
        if position is not None:
            if position < 0 or position > self.lenght + 1:
                return False

        new_node = self._create_node(node)

        # Create the list
        if self.head is None:
            self.head = new_node
            return True

        # Insert at the end of the list
        if position in [None, self.lenght + 1]:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            return True

        # Insert in a given position
        if position not in [0, None]:
            posterior_node, previous_node = self._find_position(position)
            new_node.next = posterior_node
            previous_node.next = new_node
            return True

        # Insert in position 0
        temporary = self.head
        self.head = new_node
        self.head.next = temporary
        del temporary
        return True

    def _delete_node(self, position=None):
        if position is not None:
            if position < 0 or position > self.lenght:
                return False

        current_node = self.head
        previous_node = None

        if position not in [None, self.lenght + 1]:
            posterior_node, previous_node = self._find_position(position)

            if previous_node is None:
                temporary = self.head.next
                self.head = temporary
                return True

            previous_node.next = posterior_node.next
            return True

        # If position is None delete the last Node
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        del current_node
        return True

    # PUBLIC METHODS --------------------------------------------------------------------------------------

    def show(self):
        current_node = self.head

        cont = 1
        while True:
            if current_node is None:
                break
            print("-"*30)
            print(f"\033[33mPOSITION → {cont}\033[30m", f"\n{current_node.data}")
            current_node = current_node.next
            cont += 1

    def add_node(self, node, position=None):
        validation = self._insert_node(node, position)

        if validation is True:
            self._len_linked_list()
            return
        raise IndexError("Index out of range")

    def del_node(self, position=None):
        validation = self._delete_node(position)

        if validation is True:
            self._len_linked_list()
            return
        raise IndexError("Index out of range")


# --------------------------------------------------------------------------------------------------------

class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__passaword = password

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__passaword

    @password.setter
    def password(self, new_password):
        self.__passaword = new_password

    def __str__(self):
        return f"""Name: {self.name}
Email: {self.email}
Password: {self.password}"""

    def change_password(self, new_password):
        print("Your current password")
        confirmation = input("→ ").strip()
        if confirmation != self.__passaword:
            return print("\033[31mDenied\033[30m")
        self.password = new_password
