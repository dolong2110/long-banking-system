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
    
    def test_is_valid_password(self):
        self.assertTrue(is_valid_password("21101998Abc."))
        self.assertTrue(is_valid_password("26102003@Abcd")) 
        self.assertTrue(is_valid_password("aA^U@UgVVE~An%eMxnzN#SAJ^^hG=p3CRuT875B`o6=%c36n*@=JW7c9mH~_SPPa%9nQAAvnLAvfPCjThG`QhtsG#gS=Wymkg#~q"))
        self.assertFalse(is_valid_password("21101998Abc"))  # not have special characters
        self.assertFalse(is_valid_password("21101998abc."))  # not have upper case letters
        self.assertFalse(is_valid_password("26102003_abcd"))  # not have upper case letters
        self.assertFalse(is_valid_password("abcd1234"))  # not have special characters and upper case letters
        self.assertFalse(is_valid_password("dochautuan@gmail.com"))  # not have upper letters
        self.assertFalse(is_valid_password("OPTIMIZATION@1234"))  # not have lower letters
        self.assertFalse(is_valid_password("tuandz"))  # not have enough characters
        self.assertFalse(is_valid_password("21101998Abc. "))  # not have space character
        self.assertFalse(is_valid_password("_D3ns3J+c/3rD=FJ/$#/-hh~y4svT$8Kuner-aF&KD23ZXLrL#w-%aVKwc'fiz5kM7i=FRaHFyYB*6/aw8-rTda$RtWwxbUnwq`+tuan")) # having more than 100 characters

    
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
