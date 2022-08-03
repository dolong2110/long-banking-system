from unittest import TestCase

import utils

class Test(TestCase):
    def test_is_valid_name(self):
        self.assertTrue(utils.is_valid_name("long", 4))
        self.assertFalse(utils.is_valid_name("long", 3))