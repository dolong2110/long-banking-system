import datetime
import json
import random
from collections import defaultdict
from os.path import exists
from typing import List, Optional

import consts


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



class Users:

    def __init__(self):
        self.raw_data = self._get_data()
        self.data = UsersData(self.raw_data)

    def _get_data(self):
        """
        Reads raw_data' information from the data file
        """
        if not exists(consts.USERS_DATA_PATH):
            return {}

        file = open(consts.USERS_DATA_PATH, "r")
        users_data = file.read()

        # convert string json to python object
        return json.loads(users_data)

    def update_data(self, _data) -> None:
        """
        Writes the bank information into the data file
        """

        file = open(consts.USERS_DATA_PATH, "w")
        json_data = json.dumps(_data)
        file.write(json_data)

    def create_new(self, user_information: defaultdict[str]) -> str:
        """
        Create new user with the given information
        """

        new_account_number = self.generate_account_number()
        while new_account_number in self.data.users_dict:
            new_account_number = self.generate_account_number()

        today_date = datetime.date.today().strftime("%d/%m/%Y")
        user_information["account_number"] = new_account_number
        user_information["issued_date"] = today_date
        self.raw_data[new_account_number] = user_information
        self.update_data(self.raw_data)

        return new_account_number

    def delete_user(self, account_number):
        self.raw_data.pop(account_number)
        self.update_data(self.raw_data)
        self.data.delete(account_number)


    @staticmethod
    def generate_account_number():
        """
        Generates a new unique account number
        It includes first 8 numbers of the bank and 8 random numbers
        """

        new_number = []
        for _ in range(consts.ACCOUNT_NUMBER_LEN):
            new_number.append(str(random.randint(0, 9)))

        return ''.join(new_number)

    def update_information(self, account_number: str, field: str, change: str):
        """
        changes the information of user.
        """

        self.raw_data[account_number][field] = change
        self.update_data(self.raw_data)
        self.data.update(account_number, self.raw_data[account_number])