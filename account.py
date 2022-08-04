import time
from collections import defaultdict
from typing import List, Optional

import maskpass

import sorts
from consts import *
import utils
import interface

import models

def authentication(privilege: str) -> (Optional[models.Users], int):
    """
    login or create new banking account
    """

    interface.clean_terminal_screen()

    print(utils.greeting())
    print(" Welcome to Long's Bank\n")
    print("Please choose 1 if you already have an account or 2 if you want to create a new one")
    print("  ┌─────────────┐  ╭──────────────────╮                  ")
    print("  │             │  │ ▶︎ 1 • Login     │                ")
    print("  │  L O N G    │  ├──────────────────┴────────────╮     ")
    print("  │  T U A N    │  │ ▶︎ 2 • Create New Account     │   ")
    print("  │  B A N K    │  ├──────────────────┬────────────╯     ")
    print("  │             │  │ ▶︎ 3 • Exit      │                ")
    print("  └─────────────┘  ╰──────────────────╯                  ")


    failed_attempt = FAILED_ATTEMPT
    user_choice = ""
    while failed_attempt:
        user_choice = input("☞ Enter your choice: ")
        if user_choice not in AUTHENTICATION_CHOICES:
            failed_attempt -= 1
            print("Wrong choice!!! Please choose only 1 to 3")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong choice many times, please wait few minutes to do it again")
        return None, -1

    users = models.Users(privilege)
    user_index = -1

    if user_choice == "1":
        if not users.data:
            print("There are no account yet!!!")
            return None, -1

        print("You want to login your account")
        account_number = ""
        failed_attempt = FAILED_ATTEMPT
        while failed_attempt:
            account_number = input("☞ Please enter your bank account: ")
            if account_number not in users.users_set:
                failed_attempt -= 1
                print("Account does not exist!!! Please enter your own account")
                print("You have %d try left!!!" % failed_attempt)
            else:
                break

        if not failed_attempt:
            print("You enter wrong choice many times, please wait few minutes to login again")
            return None, -1

        user_index = sorts.binary_search(users.data, ACCOUNT_NUMBER, account_number)
        if user_index == -1:
            print("You enter wrong choice many times, please wait few minutes to login again")
            return None, -1

        user = users.data[user_index]
        print(utils.greeting())
        print(" %s" % account_number)
        failed_attempt = FAILED_ATTEMPT
        hashed_password = user[PASSWORD]
        while failed_attempt:
            password = maskpass.askpass(prompt="☞ Please enter your password: ")
            if not utils.check_password(password, hashed_password):
                failed_attempt -= 1
                print("Wrong password!!! Please try another one")
                print("You have %d try left!!!" % failed_attempt)
            else:
                break

        if not failed_attempt:
            print("You enter wrong password many times, please wait few minutes to login again")
            return None, -1

        print("Successfully login!!!")
        print("Welcome back %s!!!" % user[FIRST_NAME])

    if user_choice == "2":
        print("You want to create new bank account online")
        print("Please enter required information correctly, make sure all information you provide are true")

        first_name = get_name(FIRST_NAME_MAX_LEN, FAILED_ATTEMPT, "first")
        if not first_name:
            return None, -1

        # Some people may not have middle name
        middle_name = ""
        middle_name = get_name(MIDDLE_NAME_MAX_LEN, FAILED_ATTEMPT, "middle")

        last_name = get_name(LAST_NAME_MAX_LEN, FAILED_ATTEMPT, "last")
        if not last_name:
            return None, -1

        gender = get_gender(GENDER_SET_CHOICE)
        if not gender:
            return None, -1
        
        date_of_birth = get_date_of_birth()
        if not date_of_birth:
            return None, -1

        phone_number = get_phone_number()
        if not phone_number:
            return None, -1

        email = get_email()

        password = get_password(utils.generate_hashed_password(""))
        if not password:
            return None, -1

        user_information = defaultdict(str)
        user_information[FIRST_NAME] = first_name
        user_information[MIDDLE_NAME] = middle_name
        user_information[LAST_NAME] = last_name
        user_information[GENDER] = gender
        user_information[DATE_OF_BIRTH] = date_of_birth
        user_information[PHONE_NUMBER] = phone_number
        user_information[EMAIL] = email
        user_information[PASSWORD] = password
        user_information[BALANCE] = "0"
        user_index = users.create_new(user_information)

        print("Successfully create new account!!!")

    if user_choice == "3":
        return None, -1

    print("Move to the next step")

    return users, user_index

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
    print("  ┌─────────────┐  ╭──────────────────╮   ")
    print("  │             │  │ ▶︎ 1 • Male      │   ")
    print("  │  L O N G    │  ├──────────────────┴─╮   ")
    print("  │  T U A N    │  │ ▶︎ 2 • Female      │   ")
    print("  │  B A N K    │  ├────────────────────┴╮   ")
    print("  │             │  │ ▶︎ 3 • Others       │   ")
    print("  └─────────────┘  ╰─────────────────────╯   ")
    
    failed_attempt = FAILED_ATTEMPT
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

    if not utils.is_valid_day([int(day), int(month), int(year)],
                              [int(current_day), int(current_month), int(current_year)]):
        return ""

    return day + "/" + month + "/" + year

def get_phone_number() -> str:
    failed_attempt = FAILED_ATTEMPT
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

    user_choice = utils.get_yes_no_choice()
    if not user_choice:
        return ""

    if user_choice == "2":
        return ""

    email = ""
    failed_attempt = FAILED_ATTEMPT
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

def get_password(previous_password: str) -> str:
    password = ""
    failed_attempt = FAILED_ATTEMPT
    while failed_attempt:
        password = maskpass.askpass(prompt="☞ Please enter your password. It should be at least 8 characters, "
                                    "contain numbers, lowercase, uppercase letters, and special characters: ")
        if not utils.is_valid_password(password):
            failed_attempt -= 1
            print("Invalid password. Please, try it again!!!")
            print("You have %d try left!!!" % failed_attempt)
        elif utils.check_password(password, previous_password):
            failed_attempt -= 1
            print("You enter same password with your previous password")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter invalid choice many times, please wait a few minutes to try it again!!!")
        password = ""

    failed_attempt = FAILED_ATTEMPT
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
