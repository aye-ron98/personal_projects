from selenium import webdriver
import booking_functions as bookings
import user_inputs
import time
from datetime import datetime


def main(url):
    user_name = user_inputs.get_user_name()
    password = user_inputs.get_password()

    destination = user_inputs.get_destination()
    arrival = user_inputs.get_arrival_date()
    departure = user_inputs.get_departure_date(arrival)
    nights = user_inputs.get_number_of_nights()
    occupants = user_inputs.get_number_of_occupants()
    check_duration = user_inputs.get_time_to_check()

    driver = webdriver.Chrome()
    driver.get(url)

    bookings.login(driver, user_name, password)
    bookings.page_navigation(driver)

    bookings.check_for_popup(driver)

    while datetime.now() < check_duration:
        bookings.check_for_bookings(driver, destination, arrival, departure, nights, occupants)

        if bookings.check_avalability(driver):
            print(bookings.print_avaliability(driver))
            break
        else:
            time.sleep(300)
            driver.refresh()
            continue


if __name__ == '__main__':
    main('https://member.embarcresorts.com/')
