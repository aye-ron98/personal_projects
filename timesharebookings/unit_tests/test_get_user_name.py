from unittest import TestCase
from unittest.mock import patch
from timesharebookings.user_inputs import get_user_name


class TestGetUserName(TestCase):

    @patch('builtins.input', return_value='my name')
    def test_get_user_name(self, _):
        self.assertEqual('my name', get_user_name())

    @patch('builtins.input', return_value='')
    def test_user_enters_blank(self, _):
        self.assertEqual('', get_user_name())

    @patch('builtins.input', return_value='5')
    def test_user_enters_number(self, _):
        self.assertEqual('5', get_user_name())

    @patch('builtins.input', return_value='@')
    def test_user_enters_special_character(self, _):
        self.assertEqual('@', get_user_name())
