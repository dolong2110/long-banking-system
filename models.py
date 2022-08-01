from collections import defaultdict
from typing import List, Optional


class Node:
    """
    Linked List Node
    """

    def __init__(self, value: str = "", data: dict={}, next=None, prev=None):
        """
        Creates the node with a value and reference to
        the next and previous node - double linked list
        """

        self.value = value
        self.information = data
        self.next = next
        self.prev = prev


class UsersData:
    """
    A user Data contains data structures to efficiently save
    all raw_data' information
    """

    def __init__(self, data: dict):
        """
        Creates the linked list contains all information
        of raw_data' account
        """

        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0
        self.users_dict = defaultdict(Node)
        self._list_to_linked_list(data)

    def _list_to_linked_list(self, data: dict) -> None:
        """
        Converts a Python List to a UsersData
        """

        for account_number in data:
            if account_number not in self.users_dict:
                node = Node(account_number, data[account_number])
                self.users_dict[account_number] = node
                self._add(node)

    def _add(self, node: Optional[Node]) -> None:
        """
        Internal method used to add new node
        """

        prev_node = self.tail.prev
        prev_node.next, self.tail.next = node, node
        node.prev, node.next = prev_node, self.tail

        self.size += 1

    def _remove(self, node: Node) -> None:
        """
        Internal method used to remove a node
        """

        nxt, prev = node.next, node.prev
        nxt.next, prev.prev = prev, nxt

        self.users_dict.pop(node.value)
        self.size -= 1
