from typing import Optional

import account
import consts
import interface
import models


def user_service(users: models.Users, account_number: str) -> Optional[models.Users]:
    interface.clean_terminal_screen()

    print("What do you want to do?")
    print("☞ Please choose among options below")
    print("  ┌─────────────┐  ╭───────────────────────────╮           ")
    print("  │  ╭┼┼╮       │  │ ▶︎ 1 • Get Information    │         ")
    print("  │  ╰┼┼╮       │  ├───────────────────────────┴────╮      ")
    print("  │  ╰┼┼╯       │  │ ▶︎ 2 • Update Information      │    ")
    print("  │             │  ├──────────────────────────────┬─╯      ")
    print("  │  L O N G    │  │ ▶︎ 3 • Change Password       │      ")
    print("  │  T U A N    │  ├────────────────────────────┬─╯        ")
    print("  │  B A N K    │  │ ▶︎ 4 • Delete Account      │        ")
    print("  │             │  ├────────────────────────────┴────╮     ")
    print("  │             │  │ ▶︎ 5 • Perform Transaction      │   ")
    print("  │             │  ├───────────────────────────┬─────╯     ")
    print("  │ ║│┃┃║║│┃║│║ │  │ ▶︎ 6 • Feedback           │         ")
    print("  │ ║│┃┃║║│┃║│║ │  ├─────────────────────────┬─╯           ")
    print("  │             │  │ ▶︎ 7 • Exit System      │           ")
    print("  └─────────────┘  ╰─────────────────────────╯             ")

    failed_attempt = consts.FAILED_ATTEMPT
    user_choice = ""
    while failed_attempt:
        user_choice = input("☞ Enter your choice: ")
        if user_choice not in consts.USER_SERVICES_CHOICES:
            failed_attempt -= 1
            print("Wrong choice!!! Please choose only from 1 to 7")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong choice many times, please wait few minutes to do it again")
        return None

    if user_choice == "1":
        _display_user_information(users.raw_data[account_number])

    if user_choice == "2":



def _display_user_information(user: dict) -> None:
    """
    Display user's information
    """

    interface.display_horizontal_line()
    print("Here is your information. You are welcome!!!")
    print("Full name: %s %s %s" % (user["last_name"], user["middle_name"], user["first_name"]))
    print("Gender: %s" % user["gender"])
    print("Date of birth: %s" % user["date_of_birth"])
    print("Phone number: %s" % user["phone_number"])
    print("Email: %s" % user["email"])
    print("Account number: %s" % user["account_number"])
    print("Issued date: %s" % user["issued_date"])

def _update_information(users: models.Users, account_number: str):
    data = users.raw_data
    print("What information you want to edit?")
    print("☞ Please choose among information listed below")
    print("  ┌─────────────┐  ╭────────────────────────╮        ")
    print("  │  ╭┼┼╮       │  │ ▶︎ 1 • First Name      │      ")
    print("  │  ╰┼┼╮       │  ├────────────────────────┴╮       ")
    print("  │  ╰┼┼╯       │  │ ▶︎ 2 • Middle Name      │     ")
    print("  │             │  ├───────────────────────┬─╯       ")
    print("  │  L O N G    │  │ ▶︎ 3 • Last Name      │       ")
    print("  │  T U A N    │  ├────────────────────┬──╯         ")
    print("  │  B A N K    │  │ ▶︎ 4 • Gender      │          ")
    print("  │             │  ├────────────────────┴──────╮     ")
    print("  │             │  │ ▶︎ 5 • Date of Birth      │   ")
    print("  │             │  ├──────────────────────────┬╯     ")
    print("  │ ║│┃┃║║│┃║│║ │  │ ▶︎ 6 • Phone Number      │    ")
    print("  │ ║│┃┃║║│┃║│║ │  ├───────────────────┬──────╯      ")
    print("  │             │  │ ▶︎ 7 • Email      │           ")
    print("  └─────────────┘  ╰───────────────────╯             ")

    failed_attempt = consts.FAILED_ATTEMPT
    user_choice = ""
    while failed_attempt:
        user_choice = input("☞ Enter your choice: ")
        if user_choice not in consts.USER_UPDATE_INFORMATION_CHOICES:
            failed_attempt -= 1
            print("Wrong choice!!! Please choose only from 1 to 7")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong choice many times, please wait few minutes to do it again")
        return None

    if user_choice == "1":
        first_name = account.get_name(consts.FIRST_NAME_MAX_LEN, consts.FAILED_ATTEMPT, "first")
        if not first_name:
            return None
