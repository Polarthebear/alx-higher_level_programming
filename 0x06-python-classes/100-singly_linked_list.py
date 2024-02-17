#!/usr/bin/python3
"""Class that defines a node of a singly linked list."""

class Node:
    """Representing node of singly linked list."""
    def __init__(self, data, next_node=None):
        """Initializing the node.

        Args:
            data (int): Data of the next node
            next_node (None): Next node
        """
        self.data = data
        self.next_node = next_node


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        """Setting data attribute."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value


    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setting next node attribute."""
        if not isinstance(value, None) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class representing a sinlgy linked list."""
    def __init__(self):
        """Initialize instance."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new node to the list."""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new


    def __str__(self):
        """Defing the print rep of the list."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
