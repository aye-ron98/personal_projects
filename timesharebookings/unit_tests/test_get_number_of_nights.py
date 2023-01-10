from unittest import TestCase
from unittest.mock import patch
from timesharebookings.user_inputs import get_number_of_nights
import io


class TestGetNumberOfNights(TestCase):

    @patch('builtins.input', return_value='5')
    def test_get_number_of_nights(self, _):
        self.assertEqual('5', get_number_of_nights())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='not a number')
    def test_invalid_number_of_nights(self, _, mock_print):
        run_function = get_number_of_nights()
        this_gets_printed = mock_print.getvalue()
        expected = "This value must be a whole number!\n"
        self.assertEqual(None, run_function)
        self.assertEqual(expected, this_gets_printed)

    @patch('builtins.input', return_value='0')
    def test_zero_nights(self, _):
        self.assertEqual(None, get_number_of_nights())
