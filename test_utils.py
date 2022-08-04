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
        self.assertTrue(is_valid_password("aA^U@UgVVE~An%eMxnzN#SAJ^^hG=p3CRuT875B`o6=%c36n*@=JW7c9mH~_SPPa%9"
                                          "nQAAvnLAvfPCjThG`QhtsG#gS=Wymkg#~q"))
        self.assertFalse(is_valid_password("21101998Abc"))  # not have special characters
        self.assertFalse(is_valid_password("21101998abc."))  # not have upper case letters
        self.assertFalse(is_valid_password("26102003_abcd"))  # not have upper case letters
        self.assertFalse(is_valid_password("abcd1234"))  # not have special characters and upper case letters
        self.assertFalse(is_valid_password("dochautuan@gmail.com"))  # not have upper letters
        self.assertFalse(is_valid_password("OPTIMIZATION@1234"))  # not have lower letters
        self.assertFalse(is_valid_password("tuandz"))  # not have enough characters
        self.assertFalse(is_valid_password("21101998Abc. "))  # not have space character
        self.assertFalse(is_valid_password("26102003@AbcdkRFc$Q8KtpC~eQ9u4CKg2*i38V-o%2eQfEfYkQgqH_phF`8j3hdBC7S_PMRpfXmq$v5xL3uy=742BPdwL4inegw$^Ft=6sQP'dZDbGmCoiz_9Kj`4@gFf79`aseRQzr*L65yx5u*Lg3_%#zxH8$$XJYU#sKjd2oqeH2RQUG'@7%HTCnp--*v%ZgXU~Spc-yV'pPn&LoY&joFgSfUvvHjZ3_@*/VcXzzuEfP3j&xpTtUQGEG@9ikjiE24%9R6/#xAk'8j7mb^kWTU`8rmoaNnhoA@=%6^/NFJSp39Pk*_hQBkekZWT^5qyeyQo_T#sJ^vqjPD=58R'*wXWTqr4tWy=DAg4sHHPP9Yd587$NVH&65L~U#7vKJWfmXs*+&q@D8mJe^4&4z5gLJHqCZ58jN3KzD&wDt`R'Si5qr/RP=AXX^w#h=hgaCJq`B8&AoCr~z8oH=m3gQ&Fx3&aLDE7P~YdH4uFELN*8kTpMfp+$%r4-VGQxr`*v8f'P'38&m%E5ZdBczFUCBYgAFrVEc^R'o`#F-2i47Q_qgKdnHRJcWAkfoseCxVVFjhhkLJxnd3nZyTBR5Jbi-ymM9Y7wuS&@M7#qJ`4`jve8@pR-g*aHpm$dubHfhK#H`L%dd@oMm*Bke%x6#'$5&/bn%+%RD*eP=FR+owqt-Q_ECbmS4Q^#NEegV2%yUnfLitBuadBYnva=k^$+%RMNLFiqMiw-~$`o_HTa63cT$V2kNPoot~65sJ'snX#_j'tCmxotRBNrM`*t+c+&mRgswrR~mSB@Pg-bN'&/_m'A8q9DpGDU9o=~WRiA7*obRiQrhScUb5poC*m_NG#Hn-takDrGpWr`C4*9yFXfK$*zg_Uqu@joi8cFBc'_xN*hG6HutoCzPZJu4/8ScLL5ztat6/JYM@Qg^v&pHoAatRxh6ZVGDN^NT~h#@_v9vG^2P~uPugMaiA-MmZBqo#~KeSLzoWCH`hcJiZPB/3DKb`Jfic724sXvE7o@*="))  # having more than 100 charaters


    
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
