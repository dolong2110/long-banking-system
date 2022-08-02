import account
import services

if __name__ == '__main__':
    users_data, account_number = account.authentication()
    if not users_data or not account_number:
        print("Good bye!!! See you again!!!")

    while users_data:
        users_data = services.user_service(users_data, account_number)
    print("Thank you so much for using Long bank's app, see you soon!!!")
