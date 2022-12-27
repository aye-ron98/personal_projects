"""
input_checks.py
Functions related to checking for correct user input
"""
from datetime import datetime, timedelta


def check_user_date(user_date: str) -> bool:
    """
    Check if user input is valid date format.

    :param user_date: user input string
    :precondition user_date: must be type string
    :postcondition: return True is user_date is correct format
    :postcondition: return False is user_date is incorrect format
    :return:
    """
    split_user_date = user_date.split('-')
    split_user_date.reverse()

    try:
        format_user_date = datetime.strptime('-'.join(split_user_date), "%Y-%b-%d")
    except ValueError:
        return False
    else:
        if format_user_date > datetime.now():
            return True
        else:
            return False


def get_time_to_check(duration: str) -> datetime:
    """
    Convert user input to datetime object

    :param duration: must be type string
    :precondition duration: must be number character
    :postcondition: will convert duration into datatime object
    :return: duration as a date time object
    """

    time_change = timedelta(hours=int(duration))
    new_time = datetime.now() + time_change
    return new_time


def main():
    main()


if __name__ == '__main__':
    main()
