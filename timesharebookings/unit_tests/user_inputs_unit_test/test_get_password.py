from unittest import TestCase
from unittest.mock import patch
from timesharebookings.user_inputs import get_password


class TestGetPassword(TestCase):

    @patch('builtins.input', return_value='password')
    def test_get_password(self, _):
        self.assertEqual('password', get_password())

    @patch('builtins.input', return_value='')
    def test_get_password_blank(self, _):
        self.assertEqual('', get_password())

    @patch('builtins.input', return_value='5')
    def test_get_password_number(self, _):
        self.assertEqual('5', get_password())

    @patch('builtins.input', return_value='@')
    def test_get_password_special_character(self, _):
        self.assertEqual('@', get_password())

