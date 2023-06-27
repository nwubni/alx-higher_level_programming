#!/usr/bin/python3

class Node:
    """ A node class for a linked list """

    def __init__(self, data, next_node=None):
        """ Node constructor
            Args:
                data (int): Node data
                next_node (Node): Next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets data to value
            Args:
                value (int): New data value
          """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets next node to value
            Args:
                value (Node): New data value
          """

        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list class"""

    def __init__(self):
        """A singly linked list constructor"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node to a linked list in 
            a sorted manner

        Args:
            value (Node): New node to create
        """
        node = Node(value)

        if self.__head is None:
            node.next_node = None
            self.__head = node
            return

        if self.__head.data > value:
            node.next_node = self.__head
            self.__head = node
            return

        curr = self.__head

        while (curr.next_node is not None and curr.next_node.data < value):
            curr = curr.next_node

        node.next_node = curr.next_node
        curr.next_node = node

    def __str__(self):
        """Defines a print function for the linked list"""
        output = ""
        curr = self.__head

        while curr is not None:
            output += f"{str(curr.data)}"
            output += "\n" if curr.next_node != None else ""
            curr = curr.next_node

        return output
