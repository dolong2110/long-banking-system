from typing import Optional

import consts
import models
import utils


def transaction_services(users: models.Users, account_number: str) -> Optional[models.Users]:

    print("Please choose which kind of transaction you want!!!")
    print("  ┌─────────────┐  ╭────────────────────────────╮        ")
    print("  │             │  │ ▶︎ 1 • Transfer Money      │     ")
    print("  │             │  ├───────────────────────────┬╯        ")
    print("  │  L O N G    │  │ ▶︎ 2 • Deposit Money      │      ")
    print("  │  T U A N    │  ├───────────────────────────┴─╮       ")
    print("  │  B A N K    │  │ ▶︎ 3 • Withdraw Money       │    ")
    print("  │             │  ├──────────────────┬──────────╯       ")
    print("  │             │  │ ▶︎ 4 • Exit      │               ")
    print("  └─────────────┘  ╰──────────────────╯                  ")

    failed_attempt = consts.FAILED_ATTEMPT
    user_choice = ""
    while failed_attempt:
        user_choice = input("☞ Enter your choice: ")
        if user_choice not in consts.USER_TRANSACTION_CHOICES:
            failed_attempt -= 1
            print("Wrong choice!!! Please choose only from 1 to 4")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong choice many times, please wait few minutes to do it again")
        return None

    if user_choice == "1":




def transfer_money(users, account_number: str) -> Optional[models.Users]:




def _transfer_internal(users, account_number: str) -> Optional[models.Users]:
    failed_attempt = consts.FAILED_ATTEMPT
    received_account_number = ""
    while failed_attempt:
        received_account_number = input("☞ Enter the received account number: ")
        if not utils.is_valid_account_number(received_account_number):
            failed_attempt -= 1
            print("Invalid account number!!!")
            print("You have %d try left!!!" % failed_attempt)
        elif received_account_number == account_number:
            failed_attempt -= 1
            print("It is your own account, please try it again!!!")
            print("You have %d try left!!!" % failed_attempt)
        elif received_account_number not in users.raw_data:
            failed_attempt -= 1
            print("Account does not exist!!!")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong account number many times, please wait few minutes to do it again")
        return None

