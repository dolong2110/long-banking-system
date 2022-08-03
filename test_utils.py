from unittest import TestCase

from utils import *


class Test(TestCase):

    # def test_greeting(self):
    #     self.fail()
    #
    #
    # def test_generate_hashed_password(self):
    #     self.fail()
    #
    #
    # def test_check_password(self):
    #     self.fail()


    def test_is_valid_name(self):
        self.countTestCases()
        self.assertTrue(is_valid_name("long", 4))
        self.assertTrue(is_valid_name("도주용", 4))
        self.assertFalse(is_valid_name("long", 3))  # exceed length
        self.assertFalse(is_valid_name("long%", 6))  # contain special character
        self.assertFalse(is_valid_name("long#", 6))  # contain special character
        self.assertFalse(is_valid_name("""lon"g""", 6))  # contain special character
        self.assertFalse(is_valid_name("!long", 6))  # contain special character
        self.assertFalse(is_valid_name("long'", 6))  # contain special character
        self.assertFalse(is_valid_name("long1", 6))  # contain number


    # def test_get_temporal(self):
    #     self.fail()
    #
    #
    # def test_is_valid_day(self):
    #     self.fail()
    #
    #
    # def test_is_valid_phone_number(self):
    #     self.fail()
    #
    #
    # def test_is_valid_email(self):
    #     self.fail()
    #
    #
    # def test_is_valid_password(self):
    #     self.fail()
    #
    #
    # def test_is_valid_account_number(self):
    #     self.fail()
    #
    #
    # def test_get_yes_no_choice(self):
    #     self.fail()
    #
    #
    # def test_is_valid_balance(self):
    #     self.fail()
    #
    #
    # def test_is_valid_message(self):
    #     self.fail()
    #
    #
    # def test_proceed_next(self):
    #     self.fail()