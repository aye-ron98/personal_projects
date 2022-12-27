"""
input_checks.py
Functions related to checking for correct user input
"""
from datetime import datetime


def check_user_date(user_date: str) -> bool:
    """
    Check if user input is valid date format. will not modify user input.

    :param user_date: user input string
    :precondition user_date: must be type string
    :postcondition: return True is user_date is correct format
    :postcondition: return False is user_date is incorrect format
    :return:
    """
    split_user_date = user_date.split('-')
    split_user_date.reverse()

    try:
        datetime.strptime('-'.join(split_user_date), "%Y-%b-%d")
    except ValueError:
        return False
    else:
        return True


def main():
    main()


if __name__ == '__main__':
    main()
