import account
import messages
import models
import services

if __name__ == '__main__':
    admin_data, account_number = account.authentication("admins")
    feedbacks_messages = None
    if admin_data and account_number:
        feedbacks_messages = messages.MessageQueue()

    users = models.Users()
    while admin_data:
        admin_data, feedbacks_messages = services.users_services(admin_data, account_number, feedbacks_messages)

        if feedbacks_messages:
            feedbacks_messages.update()

        print("Goodbye, see you soon!!!")