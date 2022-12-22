from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import booking_functions as bookings
import user_inputs


def main(url):
    driver = webdriver.Chrome()
    driver.get(url)

    user_name = user_inputs.get_user_name()
    password = user_inputs.get_password()

    destination = user_inputs.get_destination()
    arrival = user_inputs.get_arrival_date()
    departure = user_inputs.get_departure_date(arrival)
    nights = user_inputs.get_number_of_nights()
    occupants = user_inputs.get_number_of_occupants()

    bookings.login(driver, user_name, password)
    bookings.page_navigation(driver)

    try:
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '/html/body/div[11]/div[1]/button')))
    except:
        pass
    else:
        driver.find_element(By.XPATH, '/html/body/div[11]/div[1]/button').click()

    bookings.check_for_bookings(driver, destination, arrival, departure, nights, occupants)
    print(bookings.print_avaliability(driver))


if __name__ == '__main__':
    main('https://member.embarcresorts.com/')
