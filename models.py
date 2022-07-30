from collections import defaultdict
from typing import List


class Node:
    """
    Linked List Node
    """

    def __init__(self, value: str = "", next=None, prev=None):
        """
        Creates the node with a value and reference to
        the next and previous node - double linked list
        """
        self.value = value
        self.next = next
        self.prev = prev


class UsersData:
    """
    A user Data contains data structures to efficiently save
    all raw_data' information
    """

    def __init__(self, data: List[str]):
        """
        Creates the linked list contains all information
        of raw_data' account
        """
        self.head, self.tail = Node(), Node()
        self.len = 0
        self.dict_data = defaultdict(Node)
        self._list_to_linked_list(data)

    def _list_to_linked_list(self, arr) -> None:
        """
        Converts a Python List to a UsersData
        """

        for value in arr:
            if value not in self.dict_data:
                self._add(self.tail.prev, value)

    def _add(self, prev_node: Node, value: str) -> None:
        """
        Internal method used to add new node
        """

        nxt = prev_node.next
        add_node = Node(value)
        prev_node.next, nxt.prev = add_node, add_node
        add_node.next, add_node.prev = nxt, prev_node

        self.dict_data[value] = add_node
        self.len += 1

    def _remove(self, node: Node) -> None:
        """
        Internal method used to remove a node
        """

        nxt, prev = node.next, node.prev
        nxt.next, prev.prev = prev, nxt

        self.dict_data.pop(node.value)
        self.len -= 1
