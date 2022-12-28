from unittest import TestCase
from unittest.mock import patch
# from timesharebookings.user_inputs import get_arrival_date
from user_inputs import get_arrival_date


class TestGetArrivalDate(TestCase):

    @patch('datetime.now', return_value='2023-Jan-01 13:00:00')
    @patch('user_inputs.check_date_format', return_value='2023-Jan-01 13:00:00')
    @patch('builtins.input', return_value='01-Jan-2023')
    def test_get_arrival_date(self, _, __):
        self.assertEqual('', get_arrival_date())
