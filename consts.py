BANK_PREFIX = "21101998"
ACCOUNT_CONFIGS = {"users": {"file_name": "users_data.json", "account_number_len": 10},
                   "admins": {"file_name": "admins_data.json", "account_number_len": 5}}
MESSAGES_DATA_PATH = "messages_data.json"
FAILED_ATTEMPT = 5
AUTHENTICATION_CHOICES = {"1", "2", "3"}
USER_SERVICES_CHOICES = {"1", "2", "3", "4", "5", "6", "7"}
ADMIN_SERVICES_CHOICES = {"1", "2", "3", "4", "5", "6", "7", "8"}
USER_UPDATE_INFORMATION_CHOICES = {"1", "2", "3", "4", "5", "6", "7", "8"}
USER_TRANSACTION_CHOICES = {"1", "2", "3", "4"}
YES_NO_CHOICES = {"1", "2"}
GENDER_SET_CHOICE = {"1": "male", "2": "female", "3": "others"}
SALT_LEN = 12
FIRST_NAME_MAX_LEN = 256
MIDDLE_NAME_MAX_LEN = 128
LAST_NAME_MAX_LEN = 128
PHONE_NUMBER_LEN = 10
MIN_PASSWORD_LEN = 8
MAX_PASSWORD_LEN = 100
MESSAGE_MAX_CHARACTERS = 1000
MESSAGE_MAX_WORDS = 150




# repeated strings
FILE_NAME = "file_name"
ACCOUNT_NUMBER_LEN = "account_number_len"
FIRST_NAME = "first_name"
MIDDLE_NAME = "middle_name"
LAST_NAME = "last_name"
GENDER = "gender"
DATE_OF_BIRTH = "date_of_birth"
PHONE_NUMBER = "phone_number"
EMAIL = "email"
PASSWORD = "password"
BALANCE = "balance"
ACCOUNT_NUMBER = "account_number"
ISSUED_DATE = "issued_date"
MESSAGE = "message"
TIMESTAMP = "timestamp"
TIME = "time"

# ADMIN
FIELDS_SEARCH = {"1": ACCOUNT_NUMBER, "2": BALANCE, "3": FIRST_NAME}