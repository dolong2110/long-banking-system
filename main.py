import account
import messages
import services

if __name__ == '__main__':
    users_data, account_number = account.authentication()
    if not users_data or not account_number:
        print("Good bye!!! See you again!!!")

    feedbacks = messages.MessageQueue()

    while users_data and feedbacks:
        users_data, feedbacks = services.user_service(users_data, account_number, feedbacks)
    print("Thank you so much for using Long bank's app, see you soon!!!")
