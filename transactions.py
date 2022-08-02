from typing import Optional

import consts
import models
import utils


def transaction_services(users: models.Users, account_number: str) -> models.Users:

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
        return users

    if user_choice == "1":
        users = transfer_money(users, account_number)

    return users

def transfer_money(users, account_number: str) -> models.Users:
    return _transfer_internal(users, account_number)



def _transfer_internal(users, account_number: str) -> models.Users:
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
        return users

    receiver = users.raw_data[received_account_number]
    receiver_balance = float(receiver["balance"])
    receiver_name = receiver_user["last_name"] + " " + receiver_user["middle_name"] + " " + receiver_user["first_name"]
    print(f"Account number: {received_account_number}")
    print(f"Account holder: {receiver_name}")

    print("☞ Do you want to proceed? if YES press 1 or 2 if NO")
    user_choice = utils.get_yes_no_choice()
    if not user_choice:
        print("Finish action!!!")
        return users

    if user_choice == "2":
        print("Finish action!!!")
        return users

    user = users.raw_data[account_number]
    user_balance = float(user["balance"])
    transfer_money = _get_money_transfer(user_balance)
    user_name = user["last_name"] + " " + user["middle_name"] + " " + user["first_name"]

    print("Transaction information!!!")
    print(f"Sender: {user_name}")
    print(f"Received account number: {received_account_number}")
    print(f"Receiver: {receiver_name}")
    print(f"Amount transfer: {transfer_money}")

    print("Do you confirm?")
    user_choice = utils.get_yes_no_choice()
    if not user_choice:
        print("Finish action!!!")
        return users

    if user_choice == "2":
        print("Finish action!!!")
        return users

    receiver_balance += transfer_money
    user_balance -= transfer_money

    users.update_information(account_number, "balance", str(user_balance))
    users.update_information(received_account_number, "balance", str(receiver_balance))

    print("Successfully transfer the money!!!")
    print(f"Your balance now is: {user_balance}")

    return users

def _get_money_transfer(balance: float) -> float:
    failed_attempt = consts.FAILED_ATTEMPT
    money = 0
    while failed_attempt:
        money = input("Please choose the amount of money you want to transfer: ")
        if not utils.is_valid_balance(money):
            failed_attempt -= 1
            print("Invalid money, it must be a number!!!")
            print("You have %d try left!!!" % failed_attempt)
        elif float(money) > balance:
            failed_attempt -= 1
            print("Exceeds your current balance, try another one!!!")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You failed to choose money amount many times, please wait few minutes to do it again")
        return 0

    return float(money)