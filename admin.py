import account
import messages
import models
import services

if __name__ == '__main__':
    admin_data, user_index = account.authentication("admins")
    feedbacks_messages = None
    if admin_data and user_index != -1:
        feedbacks_messages = messages.MessageQueue()

    users = models.Users()
    while admin_data:
        admin_data, feedbacks_messages = services.admins_services(admin_data, users, user_index, feedbacks_messages)

    feedbacks_messages.update()

    print("Goodbye, see you soon!!!")