import datetime
import bcrypt

import consts


def greeting() -> str:
    """
    determine current time and choose appropriate greeting sentence
    """

    current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
    hour_min_sec = current_time.split(':')
    hours = int(hour_min_sec[0])

    if 2 <= hours < 12:
        return "Good morning!!!"
    if 12 <= hours < 18:
        return "Good afternoon!!!"
    if 18 <= hours < 22:
        return "Good evening!!!"
    return "Hello!!!"

def generate_hashed_password(plain_text_password: str) -> str:
    """
    encrypted password with random salt using bcrypt algorithms
    """

    return bcrypt.hashpw(str.encode(plain_text_password), bcrypt.gensalt(consts.SALT_LEN)).decode()

def check_password(plain_text_password: str, hashed_password: str) -> bool:
    """
    check password with password saved in DB
    """

    return bcrypt.checkpw(str.encode(plain_text_password), str.encode(hashed_password))

def is_valid_name(name: str, max_len: int) -> bool:
    if len(name) > max_len or len(name) == 0:
        return False

    set_character = set(name)
    for character in set_character:
        if character in consts.NOT_ALLOW_NAME_CHARACTER:
            return False
    return True

if __name__ == '__main__':
    print(greeting())
    print(generate_hashed_password("longdeptrai"))
    print(check_password("longdeptrai", "$2b$12$nNeZrual6HCn2KSu8OroyenyizjXqckFn8UtOl5X.zkSAxFVO6/JS"))
    print(check_password("longdeptraii", "$2b$12$nNeZrual6HCn2KSu8OroyenyizjXqckFn8UtOl5X.zkSAxFVO6/JS"))
    print(is_valid_name("abcsde%", 100))
    print(is_valid_name("""a"a""", 3))
    print(is_valid_name("!asds", 6))
    print(is_valid_name("long", 100))
    print(is_valid_name("asdkljafjlaskd", 100))
    print(is_valid_name("asdkljafjlaskd", 5))
    print(is_valid_name("1234asdvsxa", 1000))
