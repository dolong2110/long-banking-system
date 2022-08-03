import account
import messages
import services

if __name__ == '__main__':
    users_data, account_number = account.authentication()
    if not users_data or not account_number:
        print("Good bye!!! See you again!!!")

    feedbacks_messages = messages.MessageQueue()

    while users_data and feedbacks_messages:
        users_data, feedbacks_messages = services.user_service(users_data, account_number, feedbacks_messages)
        
    feedbacks_messages.update()
    print("Thank you so much for using Long bank's app, see you soon!!!")
