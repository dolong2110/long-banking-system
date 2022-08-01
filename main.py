import account


if __name__ == '__main__':
    users_data, account_number = account.authentication()
    if not users_data or not account_number:
        print("Good bye!!! See you again!!!")

