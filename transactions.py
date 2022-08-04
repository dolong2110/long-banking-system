from typing import Optional

import sorts
from consts import *
import models
import utils


def transaction_services(users: models.Users, user_index: int) -> models.Users:

    print("Please choose which privilege of transaction you want!!!")
    print("  ┌─────────────┐  ╭───────────────────────────╮        ")
    print("  │             │  │ ▶︎ 1 • Check Balance      │     ")
    print("  │             │  ├───────────────────────────┴╮        ")
    print("  │             │  │ ▶︎ 2 • Transfer Money      │      ")
    print("  │  L O N G    │  ├───────────────────────────┬╯       ")
    print("  │  T U A N    │  │ ▶︎ 3 • Deposit Money      │      ")
    print("  │  B A N K    │  ├───────────────────────────┴─╮       ")
    print("  │             │  │ ▶︎ 4 • Withdraw Money       │    ")
    print("  │             │  ├──────────────────┬──────────╯       ")
    print("  │             │  │ ▶︎ 5 • Exit      │               ")
    print("  └─────────────┘  ╰──────────────────╯                  ")

    failed_attempt = FAILED_ATTEMPT
    user_choice = ""
    while failed_attempt:
        user_choice = input("☞ Enter your choice: ")
        if user_choice not in USER_TRANSACTION_CHOICES:
            failed_attempt -= 1
            print("Wrong choice!!! Please choose only from 1 to 4")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong choice many times, please wait few minutes to do it again")
        return users

    if user_choice == "1":
        print(f"Your current account balance is: {users.data[user_index][BALANCE]}")
        utils.proceed_next()

    if user_choice == "2":
        users = transfer_money(users, user_index)
        
    if user_choice == "3":
        users = deposit_money(users, user_index)

    if user_choice == "4":
        users = withdraw_money(users, user_index)

    if user_choice == "5":
        print("Finish action!!!")
        return users

    return users

def transfer_money(users: models.Users, user_index: int) -> models.Users:
    return _transfer_internal(users, user_index)

def deposit_money(users, user_index: int) -> models.Users:
    deposit = _get_money(float('inf'))
    if not deposit:
        print("Failed to deposit money into bank")
        return users
        
    print(f"Do you want to proceed to transfer {deposit} into your bank account?")
    user_choice = utils.get_yes_no_choice()
    if not user_choice:
        print("Finish action!!!")
        return users

    if user_choice == "2":
        print("Finish action!!!")
        return users

    user = users.data[user_index]
    current_balance = user[BALANCE]
    expect_balance = float(current_balance) + float(deposit)
    print(f"After depositing your balance will be: {expect_balance}")

    print("Do you confirm to deposit?")
    user_choice = utils.get_yes_no_choice()
    if not user_choice:
        print("Finish action!!!")
        return users

    if user_choice == "2":
        print("Finish action!!!")
        return users

    users.update_information(user_index, BALANCE, str(expect_balance))
    print("Successfully deposit the money!!!")
    print(f"Your balance now is: {expect_balance}")

    return users

def withdraw_money(users: models.Users, user_index: int) -> models.Users:
    user = users.data[user_index]
    current_balance = float(user[BALANCE])
    withdraw = _get_money(current_balance)
    if not withdraw:
        print("Failed to withdraw money from bank")
        return users

    print(f"Do you want to proceed to withdraw {withdraw} from your bank account?")
    user_choice = utils.get_yes_no_choice()
    if not user_choice:
        print("Finish action!!!")
        return users

    if user_choice == "2":
        print("Finish action!!!")
        return users

    expect_balance = float(current_balance) - float(withdraw)
    print(f"After withdrawing your balance will be: {expect_balance}")

    print("Do you confirm to withdraw?")
    user_choice = utils.get_yes_no_choice()
    if not user_choice:
        print("Finish action!!!")
        return users

    if user_choice == "2":
        print("Finish action!!!")
        return users

    users.update_information(user_index, BALANCE, str(expect_balance))
    print("Successfully withdraw the money!!!")
    print(f"Your balance now is: {expect_balance}")

    return users

def _transfer_internal(users: models.Users, user_index: int) -> models.Users:
    failed_attempt = FAILED_ATTEMPT
    receiver_account_number = ""
    account_number = users.data[user_index][ACCOUNT_NUMBER]
    while failed_attempt:
        receiver_account_number = input("☞ Enter the received account number: ")
        if not utils.is_valid_account_number(receiver_account_number, "users"):
            failed_attempt -= 1
            print("Invalid account number!!!")
            print("You have %d try left!!!" % failed_attempt)
        elif receiver_account_number == account_number:
            failed_attempt -= 1
            print("It is your own account, please try it again!!!")
            print("You have %d try left!!!" % failed_attempt)
        elif receiver_account_number not in users.users_set:
            failed_attempt -= 1
            print("Account does not exist!!!")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong account number many times, please wait few minutes to do it again")
        return users

    receiver_index = sorts.binary_search(users.data, ACCOUNT_NUMBER, receiver_account_number)

    receiver = users.data[receiver_index]
    receiver_balance = float(receiver[BALANCE])
    receiver_name = receiver[LAST_NAME] + " " + receiver[MIDDLE_NAME] + " " + receiver[FIRST_NAME]
    print(f"Account number: {receiver_account_number}")
    print(f"Account holder: {receiver_name}")

    print("☞ Do you want to proceed? if YES press 1 or 2 if NO")
    user_choice = utils.get_yes_no_choice()
    if not user_choice:
        print("Finish action!!!")
        return users

    if user_choice == "2":
        print("Finish action!!!")
        return users

    user = users.data[user_index]
    user_balance = float(user[BALANCE])
    transfer_money = _get_money(user_balance)
    if not transfer_money:
        print("Finish action!!!")
        return users
    
    user_name = user[LAST_NAME] + " " + user[MIDDLE_NAME] + " " + user[FIRST_NAME]

    print("Transaction information!!!")
    print(f"Sender: {user_name}")
    print(f"Received account number: {receiver_account_number}")
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

    users.update_information(user_index, BALANCE, str(user_balance))
    users.update_information(receiver_index, BALANCE, str(receiver_balance))

    print("Successfully transfer the money!!!")
    print(f"Your balance now is: {user_balance}")

    return users

def _get_money(balance: float) -> float:
    failed_attempt = FAILED_ATTEMPT
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