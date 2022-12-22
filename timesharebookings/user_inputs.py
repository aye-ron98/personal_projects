"""
functions related to getting user inputs for program to execute
"""
from datetime import datetime
from datetime import date


def get_user_name():
    """
    Takes user input and returns it as a string. Function does not store any user information.

    :return: user input as a string
    """

    user_name = input('Enter your embarc user name: ')

    return user_name


def get_password():
    """
    Takes user input and returns it as a string. Function does not store any user information.

    :return: user input as a string
    """

    password = input('Enter your embar account password: ')

    return password


def get_arrival_date():
    """
    Takes user input and returns it as a string.

    Will check user input for date entery for DD-month-YYYY format. Informs user to try again if false.
    Will check user input for date entery to ensure date is equal or grater than current date. Informs user to try again if false.

    :return: user input as a string
    """

    arrival_date = input('Enter your arrival date in DD-month-YYYY format\n'
                         'for example 01-Jan-2023: ').title()

    formatted_arrival_date = check_date_format(arrival_date)

    if formatted_arrival_date is None:
        return
    if datetime.now() <= formatted_arrival_date:
        return arrival_date, True
    else:
        print('Your arrival date cannot be in the past'), False


def get_departure_date(arrival):
    """
    Takes user input and returns it as a string.

    Will check user input for date entery for DD-month-YYYY format. Informs user to try again if false.
    Will check user input for date entery to ensure date is equal or grater than current date. Informs user to try again if false.

    :param arrival: the arrival date
    :precondition: must be a sting in DD-month-YYYY format
    :postcondition: returns the departure date and True if preconditons are met
    :postconditoin: returns False and a message to user that departure cannot be before arrival
    if preconditions are not met
    :return: user input as a string and a Boolean
    """

    departure_date = input('Enter your departure date in DD-month-YYYY format\n'
                           'for example 01-Jan-2023: ').title()

    formatted_departure_date = check_date_format(departure_date)
    formatted_arrival_date = check_date_format(arrival)

    if formatted_departure_date is None:
        return
    if formatted_arrival_date < formatted_departure_date:
        return departure_date, True
    else:
        print('Your arrival date cannot be in the past'), False


def get_number_of_nights():
    """
    Takes user input and returns input as a string

    :return: user input as a string
    """

    nights = input('Enter number of nights you are staying: ')

    if check_number_format(nights) is not None:
        return nights


def get_number_of_occupants():
    """
    Takes user input and returns input as a string

    :return: user input as a string
    """

    occupants = input('How many people will be staying?: ')

    if check_number_format(occupants) is not None:
        return occupants


def check_date_format(user_date):
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
        return
    else:
        return date_object


def check_number_format(user_number):
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
    print(get_number_of_occupants())


if __name__ == '__main__':
    main()
