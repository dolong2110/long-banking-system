import datetime
import bcrypt
from typing import List

import consts


def greeting() -> str:
    """
    determine current time and choose appropriate greeting sentence
    """

    current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
    hour_min_sec = current_time.split(':')
    hours = int(hour_min_sec[0])

    if 2 <= hours < 12:
        return "Good morning!!!"
    if 12 <= hours < 18:
        return "Good afternoon!!!"
    if 18 <= hours < 22:
        return "Good evening!!!"
    return "Hello!!!"

def generate_hashed_password(plain_text_password: str) -> str:
    """
    encrypted password with random salt using bcrypt algorithms
    """

    return bcrypt.hashpw(str.encode(plain_text_password), bcrypt.gensalt(consts.SALT_LEN)).decode()

def check_password(plain_text_password: str, hashed_password: str) -> bool:
    """
    check password with password saved in DB
    """

    return bcrypt.checkpw(plain_text_password.encode(), hashed_password.encode())

def is_valid_name(name: str, max_len: int) -> bool:
    if len(name) > max_len or len(name) == 0:
        return False

    set_character = set(name)
    for character in set_character:
        if character in consts.NOT_ALLOW_NAME_CHARACTER:
            return False
    return True

def get_temporal(temporal: str, max_time: int) -> str:
    failed_attempt = consts.FAILED_ATTEMPT
    time = ""
    while failed_attempt:
        time = input("☞ Please enter the %s you was born: " % temporal)
        if not time.isnumeric():
            failed_attempt -= 1
            print("Invalid type of year, you should enter a valid positive integer number")
            print("You have %d try left!!!" % failed_attempt)
        elif int(time) > max_time:
            failed_attempt -= 1
            print("Invalid year, you cannot born after %d" % max_time)
            print("You have %d try left!!!" % failed_attempt)
        else:
            break

    if not failed_attempt:
        print("You enter invalid choice many times, please wait a few minutes to try it again!!!")
        time = ""

    result = [""]
    if temporal == "year":
        result = ["0" for _ in range(4)]
        i = 3
        for digit in time[::-1]:
            result[i] = digit
            i -= 1
    else:
        result = ["0" for _ in range(2)]
        i = 1
        for digit in time[::-1]:
            result[i] = digit
            i -= 1

    return "".join(result)

def is_valid_day(date: List[int], current_date: List[int]) -> bool:

    day, month, year = date
    if month < 1 or month > 12:
        print("You enter invalid month\n")
        return False

    max_day_in_month = 0
    if month in {1, 3, 5, 7, 8, 10, 12}:
        max_day_in_month = 31
    elif month in {4, 6, 9, 11}:
        max_day_in_month = 30
    elif year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
        max_day_in_month = 29
    else:
        max_day_in_month = 28

    if day < 1 or day > max_day_in_month:
        print("you enter invalid day in that month\n")
        return False

    # need 18 or higher to create
    if year > current_date[2] - 18:
        print("You need to be 18 years old to create a new account\n")
        return False

    if year < current_date[2] - 18:
        return True

    if month > current_date[1]:
        print("You need to be 18 years old to create a new account\n")
        return False

    if month < current_date[1]:
        return True

    if day < current_date[0]:
        print("You need to be 18 years old to create a new account\n")
        return False

    return True

def is_valid_phone_number(phone_number: str) -> bool:
    if len(phone_number) != consts.PHONE_NUMBER_LEN:
        print("Phone number should have length %d\n" % 10)
        return False

    if phone_number[0] != "0":
        print("Phone number should start with 0\n")
        return False

    for digit in phone_number:
        if not digit.isnumeric():
            print("%s is not a number\n" % digit)
            return False

    return True

def is_valid_email(email: str) -> bool:

    return True

def is_valid_password(password: str) -> bool:
    if len(password) < consts.MIN_PASSWORD_LEN:
        print("Password's length should be at least 8 characters!!!")
        return False

    if len(password) > consts.MAX_PASSWORD_LEN:
        print("Password's length should be smaller or equal than 100 characters!!!")
        return False

    have_number, have_lowercase, have_uppercase, have_specical_character = False, False, False, False
    for char in password:
        if char == " ":
            return False
        if char.isnumeric():
            have_number = True
        elif char.islower():
            have_lowercase = True
        elif char.isupper():
            have_uppercase = True
        elif char in consts.SPECIAL_CHARACTERS:
            have_specical_character = True

    return have_number and have_lowercase and have_uppercase and have_specical_character

if __name__ == '__main__':
    # print(greeting())
    print(generate_hashed_password("longdeptrai"))
    print(check_password("longdeptrai", "$2b$12$nNeZrual6HCn2KSu8OroyenyizjXqckFn8UtOl5X.zkSAxFVO6/JS"))
    print(check_password("longdeptraii", "$2b$12$nNeZrual6HCn2KSu8OroyenyizjXqckFn8UtOl5X.zkSAxFVO6/JS"))
    # print(is_valid_name("abcsde%", 100))
    # print(is_valid_name("""a"a""", 3))
    # print(is_valid_name("!asds", 6))
    # print(is_valid_name("long", 100))
    # print(is_valid_name("asdkljafjlaskd", 100))
    # print(is_valid_name("asdkljafjlaskd", 5))
    # print(is_valid_name("1234asdvsxa", 1000))
    # print(get_temporal("month", 12))
    # print(is_valid_password("21101998Abc!"))
    # print(is_valid_phone_number("0123456789"))
    # print(is_valid_phone_number("012345678"))
    # print(is_valid_phone_number("1123456789"))
    # print(is_valid_phone_number("012345678a"))