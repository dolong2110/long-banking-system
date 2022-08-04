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
        self.assertTrue(is_valid_password("H/iw@#LEsQ_DpvuD'x4AEHV-YA$qKKzqiS_EST@uo2nkZ6JA3p~gr`9XRxPi&N_hS~8$e3=$zLkYx_v`UKVveuMfPiiKEbk9uY*6m9eQLsjqpkvH^Sdv2~QCa@ktuRYEvC%jT2E9h&V=oQrSsg'8Qa^ZpV6%RB5=XbzGz~Eo#MqaPdd/@N5KVAo+Yb+UUFjz+/Hm$n~8Z~mqd~cLXVM2%ex~GG6%qA*M9+JC~-hzn@uapz4sDmsm2'@ZbKZhwUC`CDxc-4=XL'YFB*b+n2e`ztm6@$-t&q_j'k7Fib%&L~$EXT`L6NtM'/3fout4iAr+o`Ai$'b$UhwZYjhhnx/'MS8iR+PmaNURhSo-5s2%5Ypn~uZg7oE7Jy_NMawHWNt#*''U=J^R-NSg3QFkDnscT=KbkvcU^f'2$C7ZhmpmyjxZY_Pca_X'29W-vCnLDV4HGb7x-ziwbe^dae=KmMGa2@6B%H6889S`p8oJ5~QRkyBfR*WD4+p`R+RUN@@GG6~nK5N3-M'+8~Doqci%A*q*pWr@-D67fvtrjZPJ5YPhEJJ`CTFBPD92c/FUBq64JsZzJ7xCr=xa4f^FXgph4UoQZ7z=~vYSo@mnPj@gM^~mzEwqc8Jas4_-'c/vVar$55xn@d#h'x=XsQy$_Q*zYB28-BS`e%$4s&3~kHd3cDXiG$x&XUEdfszx/*^_ahpD49ZpMeq9yAfhz^~+%S'nwS3E7jJ&EN%XVJZx6Y9WmD6HU7`-yq`BqWyg~$c^K3WFH29pHZjSM&p*NK926$Wq32VSBwP=Xfcr3%m*HQZtntE+KYpVUXV==iX-R*8$7'tUv3F`G3#&CRkV%9UqDESYkAAh`MCSHn~C^rVQ/+9R3ojkGYzptKuhdP'nG+'@r2dCwGzqABEAWRi89VA$G2i9eo@DzRdUfEL5d@vGUv~x'pW4=gPKvbVR~se9V+zT$BA4si3o`42G2@2`z^zRXVbPV8sbyaC7YEM$PuTT3+9exCQ/"))
        self.assertFalse(is_valid_password("21101998Abc"))  # not have special characters
        self.assertFalse(is_valid_password("21101998abc."))  # not have upper case letters
        self.assertFalse(is_valid_password("26102003_abcd"))  # not have upper case letters
        self.assertFalse(is_valid_password("abcd1234"))  # not have special characters and upper case letters
        self.assertFalse(is_valid_password("dochautuan@gmail.com"))  # not have upper letters
        self.assertFalse(is_valid_password("OPTIMIZATION@1234"))  # not have lower letters
        self.assertFalse(is_valid_password("tuandz"))  # not have enough characters
        self.assertFalse(is_valid_password("21101998Abc. "))  # not have space character
        self.assertFalse(is_valid_password("26102003@AbcdkRFc$Q8KtpC~eQ9u4CKg2*i38V-o%2eQfEfYkQgqH_phF`8j3hdBC7S_PMRpfXmq$v5xL3uy=742BPdwL4inegw$^Ft=6sQP'dZDbGmCoiz_9Kj`4@gFf79`aseRQzr*L65yx5u*Lg3_%#zxH8$$XJYU#sKjd2oqeH2RQUG'@7%HTCnp--*v%ZgXU~Spc-yV'pPn&LoY&joFgSfUvvHjZ3_@*/VcXzzuEfP3j&xpTtUQGEG@9ikjiE24%9R6/#xAk'8j7mb^kWTU`8rmoaNnhoA@=%6^/NFJSp39Pk*_hQBkekZWT^5qyeyQo_T#sJ^vqjPD=58R'*wXWTqr4tWy=DAg4sHHPP9Yd587$NVH&65L~U#7vKJWfmXs*+&q@D8mJe^4&4z5gLJHqCZ58jN3KzD&wDt`R'Si5qr/RP=AXX^w#h=hgaCJq`B8&AoCr~z8oH=m3gQ&Fx3&aLDE7P~YdH4uFELN*8kTpMfp+$%r4-VGQxr`*v8f'P'38&m%E5ZdBczFUCBYgAFrVEc^R'o`#F-2i47Q_qgKdnHRJcWAkfoseCxVVFjhhkLJxnd3nZyTBR5Jbi-ymM9Y7wuS&@M7#qJ`4`jve8@pR-g*aHpm$dubHfhK#H`L%dd@oMm*Bke%x6#'$5&/bn%+%RD*eP=FR+owqt-Q_ECbmS4Q^#NEegV2%yUnfLitBuadBYnva=k^$+%RMNLFiqMiw-~$`o_HTa63cT$V2kNPoot~65sJ'snX#_j'tCmxotRBNrM`*t+c+&mRgswrR~mSB@Pg-bN'&/_m'A8q9DpGDU9o=~WRiA7*obRiQrhScUb5poC*m_NG#Hn-takDrGpWr`C4*9yFXfK$*zg_Uqu@joi8cFBc'_xN*hG6HutoCzPZJu4/8ScLL5ztat6/JYM@Qg^v&pHoAatRxh6ZVGDN^NT~h#@_v9vG^2P~uPugMaiA-MmZBqo#~KeSLzoWCH`hcJiZPB/3DKb`Jfic724sXvE7o@*=")) # having more than 100 charaters


    
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
