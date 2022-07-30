import datetime
import json
import os
import random
from os.path import exists
from typing import List

import consts
import models

class Users:

    def __init__(self):
        self.raw_data = self._get_data()
        self.data = models.UsersData(self.make_users_linked_list())

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

    def make_users_linked_list(self) -> List[str]:
        """
        This functions loads the user data and converts it
        from a dictionary to a list and then appends the
        account_number as a key from outside into the linked list
        data object.
        """

        users_list = []
        for user_account_number in self.raw_data:
            user_data = self.raw_data[user_account_number]
            user_data["account_number"] = user_account_number
            users_list.append(user_data)

        return users_list


class User:

    def __init__(self, first_name: str, last_name: str, gender: str, age: int, birth_date: str, account_number: str,
                 password: str, phone_number: str, email: str, issued_date: str, issued_place: str):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.birth_date = birth_date
        self.account_number = account_number
        self.password = password
        self.phone_number = phone_number
        self.email = email
        self.issued_date = issued_date
        self.issued_place = issued_place

    def get_information(self):
        print(f"\nPersonal Information\nFirst name: {self.first_name}\nLast_name: {self.last_name}\nAge: {self.age}\nDOB: {self.birth_date} ")

    def create_new(self, account_number_dict) -> str:
        """
        Create new user with the given information
        """

        new_account_number = self.generate_account_number()
        while new_account_number in account_number_dict:
            new_account_number = self.generate_account_number()

        return new_account_number

    @staticmethod
    def generate_account_number():
        """
        Generates a new unique account number
        It includes first 8 numbers of the bank and 8 random numbers
        """

        new_number = []
        for _ in range(8):
            new_number.append(str(random.randint(0, 9)))

        return ''.join(new_number)

    # def update_information(self):
    #     """
    #     this asks the user what to change and then
    #     changes the properties of that.
    #     """

