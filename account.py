import datetime
import json
import random
import time
from collections import defaultdict
from os.path import exists
from typing import List, Optional

import maskpass

import consts
import models
import utils
import interface

class Users:

    def __init__(self):
        self.raw_data = self._get_data()
        self.data = models.UsersData(self.make_linked_list())

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

    def make_linked_list(self) -> List[str]:
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

    def create_new(self, user_information: defaultdict(str)) -> None:
        """
        Create new user with the given information
        """

        new_account_number = self.generate_account_number()
        while new_account_number in self.data.dict_data:
            new_account_number = self.generate_account_number()

        today_date = datetime.date.today().strftime("%d/%m/%Y")
        user_information["account_number"] = new_account_number
        user_information["issued_date"] = today_date
        self.raw_data[new_account_number] = user_information
        
        self.update_data(self.raw_data)

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
    #


def authentication() -> Optional[Users]:
    """
    login or create new banking account
    """

    interface.clean_terminal_screen()
    print()

    print(utils.greeting())
    print(" Welcome to Long's Bank\n")
    print("Please choose 1 if you already have an account or 2 if you want to create a new one")
    print("  ┌─────────────┐  ╭──────────────────╮   ")
    print("  │  L O N G    │  │ ▶︎ 1 • Login     │   ")
    print("  │  T U A N    │  ├──────────────────┴────────────╮   ")
    print("  │  B A N K    │  │ ▶︎ 2 • Create New Account     │   ")
    print("  └─────────────┘  ╰───────────────────────────────╯   ")

    failed_attempt = consts.FAILED_ATTEMPT
    user_choice = ""
    while failed_attempt:
        user_choice = input("☞ Enter your choice: ")
        if user_choice not in consts.AUTHENTICATION_CHOICES:
            failed_attempt -= 1
            print("Wrong choice!!! Please choose only 1 or 2")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong choice many times, please wait few minutes to do it again")
        return None

    users = Users()

    if user_choice == "1":
        print("You want to login your account")
        failed_attempt = consts.FAILED_ATTEMPT
        account_number = ""
        while failed_attempt:
            account_number = input("☞ Please enter your bank account: ")
            if account_number not in users.data.dict_data:
                failed_attempt -= 1
                print("Account does not exist!!! Please enter your own account")
                print("You have %d try left!!!" % failed_attempt)
            else:
                break

        if not failed_attempt:
            print("You enter wrong choice many times, please wait few minutes to login again")
            return None

        user = users.raw_data["account_number"]
        print(utils.greeting())
        print(" %s" % account_number)
        failed_attempt = consts.FAILED_ATTEMPT
        hashed_password = user["password"]
        while failed_attempt:
            password = input("☞ Please enter your password: ")
            if not utils.check_password(utils.generate_hashed_password(password), hashed_password):
                failed_attempt -= 1
                print("Wrong password!!! Please try another one")
                print("You have %d try left!!!" % failed_attempt)
            else:
                break

        if not failed_attempt:
            print("You enter wrong password many times, please wait few minutes to login again")
            return None

        print("Successfully login!!!")
        print("Welcome back %d!!!" % user["first_name"])

    if user_choice == "2":
        print("You want to create new bank account online")
        print("Please enter required information correctly, make sure all information you provide are true")

        first_name = get_name(consts.FIRST_NAME_MAX_LEN, consts.FAILED_ATTEMPT, "first")
        if not first_name:
            return None

        # Some people may not have middle name
        middle_name = get_name(consts.MIDDLE_NAME_MAX_LEN, consts.FAILED_ATTEMPT, "middle")

        last_name = get_name(consts.LAST_NAME_MAX_LEN, consts.FAILED_ATTEMPT, "last")
        if not last_name:
            return None

        gender = get_gender(consts.GENDER_SET_CHOICE)
        if not gender:
            return None
        
        date_of_birth = get_date_of_birth()
        if not date_of_birth:
            return None

        phone_number = get_phone_number()
        if not phone_number:
            return None

        email = get_email()

        password = get_password()
        if not password:
            return None

        user_information = defaultdict(str)
        user_information["first_name"] = first_name
        user_information["middle_name"] = middle_name
        user_information["last_name"] = last_name
        user_information["gender"] = gender
        user_information["date_of_birth"] = date_of_birth
        user_information["phone_number"] = phone_number
        user_information["email"] = email
        user_information["password"] = password
        user_information["balance"] = "0"
        users.create_new(user_information)

    return users

def get_name(name_max_len: int, failed_attempt: int, kind: str) -> str:
    name = ""
    while failed_attempt:
        name = input("☞ Please enter your %s name: " % kind)
        if not utils.is_valid_name(name, name_max_len):
            failed_attempt -= 1
            print("Invalid %s name!!! Please try your real valid %s name" % (kind, kind))
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter invalid %s name many times, please wait few minutes to create new account again")
        name = ""

    return name

def get_gender(gender_list: List[str]) -> str:
    print("☞ Please choose among options below")
    print("  ┌─────────────┐  ╭────────────────╮   ")
    print("  │             │  │ ▶︎ 1 • Male    │   ")
    print("  │  L O N G    │  ├────────────────┴─╮   ")
    print("  │  T U A N    │  │ ▶︎ 2 • Female    │   ")
    print("  │  B A N K    │  ├──────────────────┴╮   ")
    print("  │             │  │ ▶︎ 3 • Others     │   ")
    print("  └─────────────┘  ╰───────────────────╯   ")
    
    failed_attempt = consts.FAILED_ATTEMPT
    gender = ""
    while failed_attempt:
        gender = input("☞ Please enter your choice about your gender: ")
        if gender not in gender_list:
            failed_attempt -= 1
            print("Invalid choice please read carefully, choose 1 for male, 2 for female and 3 for others")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break
    if not failed_attempt:
        print("You enter invalid choice many times, please wait a few minutes to try it again!!!")
        return ""

    if gender == "1":
        return "male"

    if gender == "2":
        return "female"

    if gender == "3":
        return "others"

    return ""

def get_date_of_birth() -> str:
    print("☞ Please enter the year, month, day when you was born respectively!!!")
    current_time = time.strftime("%d:%m:%Y")
    current_time_list = current_time.split(":")
    current_day, current_month, current_year = current_time_list

    year = utils.get_temporal("year", int(current_year))
    if not year:
        return ""
    
    month = utils.get_temporal("month", 12)
    if not month:
        return ""

    day = utils.get_temporal("day", 31)
    if not day:
        return ""

    if not utils.is_valid_day([int(day), int(month), int(year)], [int(current_day), int(current_month), int(current_year)]):
        return ""

    return day + "/" + month + "/" + year

def get_phone_number() -> str:
    failed_attempt = consts.FAILED_ATTEMPT
    phone_number = ""
    while failed_attempt:
        phone_number = input("☞ Please enter your phone number: ")
        if not utils.is_valid_phone_number(phone_number):
            failed_attempt -= 1
            print("Invalid phone number, please, try it again!!!")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break
    if not failed_attempt:
        print("You enter invalid choice many times, please wait a few minutes to try it again!!!")
        phone_number = ""

    return phone_number

def get_email() -> str:
    print("☞ Do you want to add your email? if YES press 1 or 2 if NO")
    print("  ┌─────────────┐  ╭────────────────╮   ")
    print("  │  L O N G    │  │ ▶︎ 1 • YES     │   ")
    print("  │  T U A N    │  ├───────────────┬╯   ")
    print("  │  B A N K    │  │ ▶︎ 2 • NO     │   ")
    print("  └─────────────┘  ╰───────────────╯   ")

    failed_attempt = consts.FAILED_ATTEMPT
    user_choice = ""
    while failed_attempt:
        user_choice = input("☞ Enter your choice: ")
        if user_choice not in {"1", "2"}:
            failed_attempt -= 1
            print("Wrong choice!!! Please choose only 1 or 2")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong choice many times, please wait few minutes to do it again")
        return ""

    if user_choice == "2":
        return ""

    email = ""
    failed_attempt = consts.FAILED_ATTEMPT
    while failed_attempt:
        email = input("☞ Please enter your email: ")
        if not utils.is_valid_email(email):
            failed_attempt -= 1
            print("Invalid email, please, try it again!!!")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter invalid choice many times, please wait a few minutes to try it again!!!")
        email = ""

    return email

def get_password() -> str:
    password = ""
    failed_attempt = consts.FAILED_ATTEMPT
    while failed_attempt:

        password = maskpass.askpass(prompt="☞ Please enter your password. It should be at least 8 characters, "
                                   "contain numbers, lowercase, uppercase letters, and special characters: ")

        if not utils.is_valid_password(password):
            failed_attempt -= 1
            print("Invalid password. Please, try it again!!!")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter invalid choice many times, please wait a few minutes to try it again!!!")
        password = ""

    failed_attempt = consts.FAILED_ATTEMPT
    while failed_attempt:
        re_enter_password = maskpass.askpass(prompt="☞ Please re-enter your password: ")
        if password != re_enter_password:
            failed_attempt -= 1
            print("Different with your previous password. Please, try it again!!!")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter invalid choice many times, please wait a few minutes to try it again!!!")
        password = ""

    return utils.generate_hashed_password(password)

if __name__ == '__main__':
    print(get_password())