from unittest import TestCase
from unittest.mock import patch
import io
from timesharebookings.user_inputs import get_departure_date
from freezegun import freeze_time


class TestGetDepartureDate(TestCase):

    @freeze_time('01-Jan-2023')
    @patch('builtins.input', return_value='05-Jan-2023')
    def test_get_departure_date(self, _):
        self.assertEqual('05-Jan-2023', get_departure_date('01-Jan-2023'))

    @freeze_time('01-Jan-2023')
    @patch('builtins.input', return_value='01-Jan-2022')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_invalid_date_from_past(self, mock_print, _):
        run_function = get_departure_date('01-Jan-2023')
        this_gets_printed = mock_print.getvalue()
        expected_output = "Your arrival date cannot be in the past\n"
        self.assertEqual(None, run_function)
        self.assertEqual(expected_output, this_gets_printed)

    @freeze_time('01-Jan-2023')
    @patch('builtins.input', return_value='not a format')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_invalid_date_format(self, mock_print, _):
        run_function = get_departure_date('01-Jan-2023')
        this_gets_printed = mock_print.getvalue()
        expected_output = "You must enter in a DD-month-YYYY format.\n"
        self.assertEqual(None, run_function)
        self.assertEqual(expected_output, this_gets_printed)
