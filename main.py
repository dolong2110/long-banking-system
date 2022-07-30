import time
from typing import Optional

import account
import consts
import interface
import utils


def authentication() -> Optional[account.Users]:
    """
    login or create new banking account
    """

    interface.clean_terminal_screen()
    print()

    print(utils.greeting())
    print(" Welcome to Long's Bank\n")
    print("Please choose 1 if you already have an account or 2 if you want to create a new one\n")
    print("  ┌─────────────┐  ╭──────────────────╮                ")
    print("  │  L O N G    │  │ ▶︎ 1 • Login   │               ")
    print("  │  T U A N    │  ├──────────────────┴────────────╮   ")
    print("  │  B A N K    │  │ ▶︎ 2 • Create New Account   │   ")
    print("  └─────────────┘  ╰───────────────────────────────╯   ")

    time.sleep(1)

    failed_attempt = consts.FAILED_ATTEMPT
    user_choice = ""
    while failed_attempt:
        user_choice = input("☞ Enter your choice: \n")
        if user_choice not in consts.AUTHENTICATION_CHOICES:
            failed_attempt -= 1
            print("Wrong choice!!! Please choose only 1 or 2\n")
            print("You have %d try left!!!\n" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong choice many times, please wait few minutes to do it again\n")
        return None

    print("\n")

    users = account.Users()

    if user_choice == "1":
        print("You want to login your account\n")
        failed_attempt = consts.FAILED_ATTEMPT
        bank_account = ""
        while failed_attempt:
            bank_account = input("☞ Please enter your bank account: \n")
            if bank_account not in users.data.dict_data:
                failed_attempt -= 1
                print("Account does not exist!!! Please enter your own account\n")
                print("You have %d try left!!!\n" % failed_attempt)
            else:
                break

        if not failed_attempt:
            print("You enter wrong choice many times, please wait few minutes to do it again\n")
            return None

        print(utils.greeting())
        print(" %s\n" % bank_account)
        failed_attempt = consts.FAILED_ATTEMPT
        password = ""


    if user_choice == "2":
        print("a")

    return users


# def display_menu():
#     """
#     Displays the welcome menu and asks the user for a
#     command to perform (which then performs).
#
#     This also acts as the UI and receives the information
#     regarding of the respective functions.
#     """
#
#     interface.clean_terminal_screen()
#     print()
#     print()
#
#     user_choice = input("\n  ☞ Enter your command: ")
#
#     interface.clean_terminal_screen()
#
#     if user_choice == "1":

if __name__ == '__main__':
    a = authentication()
    print(a)
