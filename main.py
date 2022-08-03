import account
import messages
import services

if __name__ == '__main__':
    users_data, account_number = account.authentication("users")
    feedbacks_messages = None
    if users_data and account_number:
        feedbacks_messages = messages.MessageQueue()

    while users_data:
        users_data, feedbacks_messages = services.users_services(users_data, account_number, feedbacks_messages)

    if feedbacks_messages:
        feedbacks_messages.update()

    print("Thank you so much for using Long bank's app, see you soon!!!")
