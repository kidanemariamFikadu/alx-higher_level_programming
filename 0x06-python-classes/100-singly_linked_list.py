#!/usr/bin/python3
class Node:
    """ A class that defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Method to initialize the node object"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Method to return node data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Mothod to set node data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Mothod to initiate next node data"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Mothod to set next node data"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ A class that defines a singly linked list"""
    def __str__(self):
        """Structure to define the linked list"""
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """Mothod to initialize the single list"""
        self.__head = None

    def sorted_insert(self, value):
        """Method to insert the node"""
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
