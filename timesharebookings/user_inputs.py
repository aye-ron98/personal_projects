"""
functions related to getting user inputs for program to execute
"""
from datetime import datetime, timedelta


def get_user_name() -> str:
    """
    Takes user input and returns it as a string. Function does not store any user information.

    :return: user input as a string
    """

    user_name = input('Enter your embarc user name: ')

    return user_name


def get_password() -> str:
    """
    Takes user input and returns it as a string. Function does not store any user information.

    :return: user input as a string
    """

    password = input('Enter your embarc account password: ')

    return password


def get_arrival_date() -> None | str:
    """
    Takes user input and returns it as a string.

    Will check user input for date entery for DD-month-YYYY format. Informs user to try again if false.
    Will check user input for date entery to ensure date is equal or grater than current date.
    Informs user to try again if false.

    :postcondition: return None if user enters incorrect format
    :postcondition: return userinput as sring if user input is in correct format
    :return: user input as a string or None
    """

    arrival_date = input('Enter your arrival date in DD-month-YYYY format\n'
                         'for example 01-Jan-2023: ').title()

    formatted_arrival_date = check_date_format(arrival_date)

    if formatted_arrival_date is None:
        return
    if datetime.now() <= formatted_arrival_date:
        return arrival_date
    else:
        print('Your arrival date cannot be in the past')


def get_departure_date(arrival) -> None | str:
    """
    Takes user input and returns it as a string.

    Will check user input for date entery for DD-month-YYYY format. Informs user to try again if false.
    Will check user input for date entery to ensure date is equal or grater than current date.
    Informs user to try again if false.

    :param arrival: the arrival date
    :precondition: must be a sting in DD-month-YYYY format
    :postcondition: returns the departure date and True if preconditons are met
    :postconditoin: returns False and a message to user that departure cannot be before arrival
    if preconditions are not met
    :return: user input as a string or None
    """

    departure_date = input('Enter your departure date in DD-month-YYYY format\n'
                           'for example 01-Jan-2023: ').title()

    formatted_departure_date = check_date_format(departure_date)
    formatted_arrival_date = check_date_format(arrival)

    if formatted_departure_date is None:
        return
    if formatted_arrival_date < formatted_departure_date:
        return departure_date
    else:
        print('Your arrival date cannot be in the past')


def get_number_of_nights() -> str | None:
    """
    Takes user input and returns input as a string

    :return: user input as a string
    """

    nights = input('Enter number of nights you are staying: ')

    if check_number_format(nights) is not None and nights != '0':
        return nights


def get_number_of_occupants() -> str | None:
    """
    Takes user input and returns input as a string

    :return: user input as a string
    """

    occupants = input('How many people will be staying?: ')

    if check_number_format(occupants) is not None and occupants != '0':
        return occupants


def get_destination() -> str:
    """
    Prompt user for destination to search for

    :return: user input as a string
    """

    destination = input('Where would you like to go? (eg Embarc® Whistler): ')

    return destination


def get_time_to_check() -> datetime:
    """
    prompts user for duration to check for rooms

    :return: user input as a date time object
    """

    check_duration = input('how long would you like to check\n'
                           'format in hours eg 1 hour = 1: ')
    duration = check_number_format(check_duration)

    if duration is not None:
        time_change = timedelta(hours=int(duration))
        new_time = datetime.now() + time_change
        return new_time


def check_date_format(user_date: str) -> datetime:
    """
    Checks format of user input to ensure it is in DD-month-YYYY format. If not informs user to correct it.
    
    :param user_date: a string
    :precondition date: must be a string
    :postcondition: if date is in correct format will return string
    :postcodition: if date is not in correct format will raise a Value error indicating user has made a mistake.
    :return: date
    """
    split_user_date = user_date.split('-')
    split_user_date.reverse()

    try:
        date_object = datetime.strptime('-'.join(split_user_date), "%Y-%b-%d")
    except ValueError:
        print('You must enter in a DD-month-YYYY format.')
    else:
        return date_object


def check_number_format(user_number: str) -> str | None:
    """
    Checks format of user input to ensure it is an integer.

    :param user_number: a string
    :precondition user_number: must be a string
    :postcondition: if user_number is an integer will it as return string
    :postcodition: if user_number is not in correct format will raise a Value error indicating user has made a mistake.
    :return: user_number as a string
    """

    try:
        int(user_number)
    except ValueError:
        print('This value must be a whole number!')
        return
    else:
        return user_number


def main():
    main()


if __name__ == '__main__':
    main()
