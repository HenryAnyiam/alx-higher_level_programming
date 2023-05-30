#!/usr/bin/python3
"""100-singly_linked_list.py module on a sorted linked list"""


class Node:
    """class Node, Node of a linked list"""

    def __init__(self, data, next_node=None):
        """initialization of class Node
        Args:
            data: node data
            next_node: node object

        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """gets private attribute data

            setter checks if data is an integer

            """
            return self.__data

        @data.setter
        def data(self, value):
            if isinstance(value, int):
                self.__data = value
            else:
                raise TypeError("data must be an integer")

        @property
        def next_node(self):
            """gets private attribute next_node

            setter checks if data is a next node object or None

            """
            
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            if isinstance(value, 100-singly_linked_list.Node):
                self.__next_node = value
            else:
                raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """class SinglyLinkedList building a linked list"""

    def __init__(self):
        """initialization of class SinglyLinkedList"""

        self.__head = []
        self.__vals = []
        self.__values = ""

    def __str__(self):
        for i in range(len(self.__vals)):
            self.__values += str(self.__vals[i])
            if i != (len(self.__vals) - 1):
                self.__values += '\n'
        return self.__values

    def sorted_insert(self, value):
        """adds a value to the list and sorts it

        Args:
            value: value to be added

        """
        self.__head.append(Node(value))
        self.__vals.append(value)
        self.__vals.sort()
