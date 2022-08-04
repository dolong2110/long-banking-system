import account
import messages
import services

if __name__ == '__main__':
    users_data, user_index = account.authentication("users")
    feedbacks_messages = None
    if users_data and user_index != -1:
        print("Hello world")
        feedbacks_messages = messages.MessageQueue()

    while users_data:
        users_data, feedbacks_messages = services.users_services(users_data, user_index, feedbacks_messages)

    if feedbacks_messages:
        feedbacks_messages.update()

    print("Thank you so much for using Long bank's app, see you soon!!!")
