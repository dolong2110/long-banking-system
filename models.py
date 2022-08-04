import datetime
import random
from collections import defaultdict
from typing import Optional

from consts import *
import utils


class Node:
    """
    Linked List Node
    """

    def __init__(self, value: str = "", data: dict = {}, next = None, prev = None):
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

    def update(self, account_number: str, data: defaultdict[str]):
        node = self.users_dict[account_number]
        node.information = data

    def delete(self, account_number: str):
        self._remove(self.users_dict[account_number])

    def swap(self, node1: Node, node2: Node) -> None:
        prev1, next1 = node1.prev, node1.next
        prev2, next2 = node2.prev, node2.next

        node1.prev, node1.next = prev2, next2
        node2.prev, node2.next = prev1, next1

        prev1.next, next1.prev = node1, node1
        prev2.next, next2.prev = node2, node2

    def _add(self, node: Node) -> None:
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


class Users:

    def __init__(self, privilege: str = "users"):

        self.privilege = privilege
        self.configs = ACCOUNT_CONFIGS[privilege]
        self.raw_data = utils.get_data_from_json(self.configs[FILE_NAME])
        self.data = UsersData(self.raw_data)

    def create_new(self, user_information: defaultdict[str]) -> str:
        """
        Create new user with the given information
        """

        new_account_number = self.generate_account_number(self.configs[ACCOUNT_NUMBER_LEN])
        while new_account_number in self.data.users_dict:
            new_account_number = self.generate_account_number(self.configs[ACCOUNT_NUMBER_LEN])

        today_date = datetime.date.today().strftime("%d/%m/%Y")
        user_information[ACCOUNT_NUMBER] = new_account_number
        user_information[ISSUED_DATE] = today_date
        self.raw_data[new_account_number] = user_information
        utils.write_data_to_json(self.raw_data, self.configs[FILE_NAME])

        return new_account_number

    def delete_user(self, account_number) -> None:
        self.raw_data.pop(account_number)
        utils.write_data_to_json(self.raw_data, self.configs[FILE_NAME])
        self.data.delete(account_number)


    @staticmethod
    def generate_account_number(account_len: int):
        """
        Generates a new unique account number
        It includes first 8 numbers of the bank and 8 random numbers
        """

        new_number = []
        for _ in range(account_len):
            new_number.append(str(random.randint(0, 9)))

        return ''.join(new_number)

    def update_information(self, account_number: str, field: str, change: str):
        """
        changes the information of user.
        """

        self.raw_data[account_number][field] = change
        utils.write_data_to_json(self.raw_data, self.configs[FILE_NAME])
        self.data.update(account_number, self.raw_data[account_number])
