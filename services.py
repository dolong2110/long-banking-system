from typing import Optional

import account
import sorts
from consts import *
import interface
import messages
import models
import transactions
import utils


def users_services(users: models.Users, user_index: int, feedbacks_messages: messages.MessageQueue) -> \
        (Optional[models.Users], Optional[messages.MessageQueue]):
    interface.clean_terminal_screen()
    interface.display_horizontal_line()

    print("What do you want to do next?")
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
    print("  │             │  ├───────────────────────┬─────────╯     ")
    print("  │ ║│┃┃║║│┃║│║ │  │ ▶︎ 6 • Feedbacks      │             ")
    print("  │ ║│┃┃║║│┃║│║ │  ├───────────────────────┴─╮             ")
    print("  │             │  │ ▶︎ 7 • Exit System      │           ")
    print("  └─────────────┘  ╰─────────────────────────╯             ")

    failed_attempt = FAILED_ATTEMPT
    user_choice = ""
    while failed_attempt:
        user_choice = input("☞ Enter your choice: ")
        if user_choice not in USER_SERVICES_CHOICES:
            failed_attempt -= 1
            print("Wrong choice!!! Please choose only from 1 to 7")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong choice many times, please wait few minutes to do it again")
        return None, feedbacks_messages

    if user_choice == "1":
        _display_user_information(users.data[user_index])

    if user_choice == "2":
        users = _update_information(users, user_index)

    if user_choice == "3":
        users = _update_password(users, user_index)

    if user_choice == "4":
        users.delete_user(user_index)
        return None, feedbacks_messages

    if user_choice == "5":
        users = transactions.transaction_services(users, user_index)

    if user_choice == "6":
        feedbacks_messages = messages.add_message(feedbacks_messages, users.data[user_index][ACCOUNT_NUMBER])

    if user_choice == "7":
        return None, feedbacks_messages

    return users, feedbacks_messages

def admins_services(admins: models.Users, users: models.Users, user_index: int,
                    feedbacks_messages: messages.MessageQueue) -> \
        (Optional[models.Users], Optional[messages.MessageQueue]):
    interface.clean_terminal_screen()
    interface.display_horizontal_line()

    print("What operation do you want to do?")
    print("☞ Please choose among admins' options below")
    print("  ┌─────────────┐  ╭───────────────────────────╮                ")
    print("  │  ╭┼┼╮       │  │ ▶︎ 1 • Get Information    │              ")
    print("  │  ╰┼┼╮       │  ├───────────────────────────┴────╮           ")
    print("  │  ╰┼┼╯       │  │ ▶︎ 2 • Update Information      │         ")
    print("  │             │  ├──────────────────────────────┬─╯           ")
    print("  │  L O N G    │  │ ▶︎ 3 • Change Password       │           ")
    print("  │  T U A N    │  ├────────────────────────────┬─╯             ")
    print("  │  B A N K    │  │ ▶︎ 4 • Delete Account      │             ")
    print("  │             │  ├────────────────────────────┴───────╮       ")
    print("  │             │  │ ▶︎ 5 • Get User's Information      │     ")
    print("  │             │  ├────────────────────────────────────┴─╮     ")
    print("  │             │  │ ▶︎ 6 • Get Information by Field      │   ")
    print("  │             │  ├────────────────────────────┬─────────╯     ")
    print("  │ ║│┃┃║║│┃║│║ │  │ ▶︎ 7 • Read Feedbacks      │             ")
    print("  │ ║│┃┃║║│┃║│║ │  ├─────────────────────────┬──╯               ")
    print("  │             │  │ ▶︎ 8 • Exit System      │                ")
    print("  └─────────────┘  ╰─────────────────────────╯                  ")

    failed_attempt = FAILED_ATTEMPT
    admin_choice = ""
    while failed_attempt:
        admin_choice = input("☞ Enter your choice: ")
        if admin_choice not in ADMIN_SERVICES_CHOICES:
            failed_attempt -= 1
            print("Wrong choice!!! Please choose only from 1 to 8")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong choice many times, please wait few minutes to do it again")
        return None, feedbacks_messages

    if admin_choice == "1":
        _display_user_information(admins.data[user_index])

    if admin_choice == "2":
        admins = _update_information(admins, user_index)

    if admin_choice == "3":
        users = _update_password(admins, user_index)

    if admin_choice == "4":
        users.delete_user(user_index)
        return None, feedbacks_messages

    if admin_choice == "5":
        account_number = _get_account_number(users)
        if not account_number:
            return users, feedbacks_messages

        user_index = sorts.binary_search(users.data, ACCOUNT_NUMBER, account_number)
        if user_index == -1:
            print("Users not exists, please try again!!!")
            return users, feedbacks_messages

        _display_user_information(users.data[user_index])

    if admin_choice == "6":
        _get_user_information_by_field(users)

    if admin_choice == "7":
        feedbacks_messages = messages.read_message(feedbacks_messages)

    if admin_choice == "8":
        return None, feedbacks_messages

    return admins, feedbacks_messages

def _display_user_information(user: dict) -> None:
    """
    Display user's information
    """

    interface.display_horizontal_line()

    print("Here is your information. You are welcome!!!")
    print("Full name: %s %s %s" % (user[LAST_NAME], user[MIDDLE_NAME], user[FIRST_NAME]))
    print("Gender: %s" % user[GENDER])
    print("Date of birth: %s" % user[DATE_OF_BIRTH])
    print("Phone number: %s" % user[PHONE_NUMBER])
    print("Email: %s" % user[EMAIL])
    print("Account number: %s" % user[ACCOUNT_NUMBER])
    print("Issued date: %s" % user[ISSUED_DATE])

    interface.display_horizontal_line()
    utils.proceed_next()


def _update_information(users: models.Users, user_index: int) -> models.Users:
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
    print("  │             │  ├──────────────────┬╯             ")
    print("  │             │  │ ▶︎ 8 • Exit      │            ")
    print("  └─────────────┘  ╰──────────────────╯              ")

    failed_attempt = FAILED_ATTEMPT
    user_choice = ""
    while failed_attempt:
        user_choice = input("☞ Enter your choice: ")
        if user_choice not in USER_UPDATE_INFORMATION_CHOICES:
            failed_attempt -= 1
            print("Wrong choice!!! Please choose only from 1 to 8")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter wrong choice many times, please wait few minutes to do it again")
        return users

    if user_choice == "1":
        first_name = account.get_name(FIRST_NAME_MAX_LEN, FAILED_ATTEMPT, "first")
        if not first_name:
            return users

        users.update_information(user_index, FIRST_NAME, first_name)
        print("Successfully update your first name!!!")

    if user_choice == "2":
        middle_name = account.get_name(FIRST_NAME_MAX_LEN, FAILED_ATTEMPT, "middle")
        if not middle_name:
            return users

        users.update_information(user_index, MIDDLE_NAME, middle_name)
        print("Successfully update your middle name!!!")

    if user_choice == "3":
        last_name = account.get_name(FIRST_NAME_MAX_LEN, FAILED_ATTEMPT, "last")
        if not last_name:
            return users

        users.update_information(user_index, LAST_NAME, last_name)
        print("Successfully update your last name!!!")

    if user_choice == "4":
        gender = account.get_gender(GENDER_SET_CHOICE)
        if not gender:
            return users

        users.update_information(user_index, GENDER, gender)
        print("Successfully update your gender!!!")

    if user_choice == "5":
        date_of_birth = account.get_date_of_birth()
        if not date_of_birth:
            return users

        users.update_information(user_index, DATE_OF_BIRTH, date_of_birth)
        print("Successfully update your date of birth!!!")

    if user_choice == "6":
        phone_number = account.get_phone_number()
        if not phone_number:
            return users

        users.update_information(user_index, PHONE_NUMBER, phone_number)
        print("Successfully update your phone number!!!")

    if user_choice == "7":
        email = account.get_email()
        if not email:
            return users

        users.update_information(user_index, EMAIL, email)
        print("Successfully update your email!!!")

    if user_choice == "8":
        return users

    print("Please check your new information")
    _display_user_information(users.data[user_index])

    return users

def _update_password(users: models.Users, user_index: int) -> models.Users:
    new_password = account.get_password(users.data[user_index][PASSWORD])
    if not new_password:
        return users

    users.update_information(user_index, PASSWORD, new_password)
    print("Successfully update new password")

    return users

def _get_account_number(users: models.Users) -> str:
    failed_attempt = FAILED_ATTEMPT
    account_number = ""
    while failed_attempt:
        account_number = input("☞ Please enter the user's account number: ")
        if not utils.is_valid_account_number(account_number, "users"):
            failed_attempt -= 1
            print("Invalid account number, please, try it again!!!")
            print("You have %d try left!!!" % failed_attempt)
        elif account_number not in users.users_set:
            failed_attempt -= 1
            print("account number does not exist, please, try it again!!!")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter invalid choice many times, please wait a few minutes to try it again!!!")
        phone_number = ""

    return account_number

def _get_user_information_by_field(users: models.Users) -> None:
    print("☞ Please choose among options below")
    print("  ┌─────────────┐  ╭────────────────────────────╮     ")
    print("  │             │  │ ▶︎ 1 • Account Number      │   ")
    print("  │  L O N G    │  ├─────────────────────┬──────╯     ")
    print("  │  T U A N    │  │ ▶︎ 2 • Balance      │          ")
    print("  │  B A N K    │  ├─────────────────────┴──╮         ")
    print("  │             │  │ ▶︎ 3 • First Name      │       ")
    print("  └─────────────┘  ╰────────────────────────╯          ")

    failed_attempt = FAILED_ATTEMPT
    user_choice = ""
    while failed_attempt:
        user_choice = input("☞ Please enter the user's account number: ")
        if user_choice not in FIELDS_SEARCH:
            failed_attempt -= 1
            print(f"You cannot search by field: {field}, please, try it again!!!")
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt or not user_choice:
        print("You enter invalid choice many times, please wait a few minutes to try it again!!!")
        phone_number = ""

    field = FIELDS_SEARCH[user_choice]
    sort_data = sorts.Sorting(users.data, field, "").arr
    if not sort_data:
        print("There are no users at that time in database")
        return

    for user in sort_data:
        _display_user_information(user)