import random

import consts

def generate_account_number():
    """
    Generates a new unique account number
    It includes first 8 numbers of the bank and 8 random numbers
    """

    new_number = [digit for digit in consts.BANK_PREFIX]
    for _ in range(8):
        new_number.append(str(random.randint(0, 9)))

    return ''.join(new_number)


if __name__ == '__main__':
    print(generate_account_number())