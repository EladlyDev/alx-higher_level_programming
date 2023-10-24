#!/usr/bin/python3
"""100-singly_linked_list
This module defins a Node class which a node of a singly linke list.
And a SinglyLinkedList class that defins a singly linked list.
"""


class Node():
    """
    This class creates a new node in a singly linked list
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if (type(data) is not int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        return self.__new_node

    @next_node.setter
    def next_node(self, value):
        if (type(value) is not Node and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__new_node = value


class SinglyLinkedList():
    """
    This class defins a singly linked list
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        newNode = Node(value)
        curr = self.__head

        if curr is None or curr.data >= value:
            newNode.next_node = curr
            self.__head = newNode
        else:
            curr = self.__head
            while (curr.next_node and curr.next_node.data < value):
                curr = curr.next_node
            newNode.next_node = curr.next_node
            curr.next_node = newNode

    def __str__(self):
        out = ""
        tmp = self.__head
        while tmp:
            out += str(tmp.data) + "\n"
            tmp = tmp.next_node
        out = out[0:-1]
        return out
