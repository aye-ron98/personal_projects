from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def login(se_driver):
    """
    login to embarc website

    :param se_driver: a webdriver for selenium framework to use
    :precondition se_driver: webdriver must be accessible by computer
    :postcondition: will login to the embarc website
    """

    username = se_driver.find_element(By.XPATH, '//*[@id="Username"]')
    username.send_keys('erwinzhang')

    password = se_driver.find_element(By.XPATH, '//*[@id="Password"]')
    password.send_keys('Safety2021')

    logon = se_driver.find_element(By.XPATH, '//*[@id="page-mobile"]/div[3]/div[2]/div/form/div[3]/div[4]/input')
    logon.click()


def page_navigation(se_driver):
    """
    Navigate webpage

    :param se_driver: a webdriver for selenium framework to use
    :precondition se_driver: webdriver must be accessible by computer
    :postcondition: will navigate to desired pages on website
    """

    navigate_to_bookings = se_driver.find_element(By.XPATH, '//*[@id="dashboard-content"]/div[2]/div/div[2]/a')
    navigate_to_bookings.click()


def check_for_bookings(se_driver, location, arrival, departure, nights, occupancy):
    """
    Check hotel site for available bookings, returns list of available bookings if
    found else notifies user none are available.

    :param se_driver: a webdriver for selenium framework to use
    :param location: a valid embrac location
    :param arrival: an arrival date greater than or equal to today's date
    :param departure: the departure date greater than the arrival date
    :param nights: number of nights user wishes to stay
    :param occupancy: number of people staying in booking
    :precondition se_driver: webdriver must be accessible by computer
    :precondition: arrival and departure must be string in DD-Month-YYYY format
    :precondition: nights and occupancy must be a number formatted as string type
    :postcondition: will check the current openings and attempt to match them against user input
    """

    destination = se_driver.find_element(By.XPATH, '//*[@id="DestinationSearchTerm"]')
    destination.send_keys(location)

    arrival_date = se_driver.find_element(By.XPATH, '//*[@id="Booking_CheckInFromDate"]')
    arrival_date.clear()
    arrival_date.send_keys(arrival)

    departure_date = se_driver.find_element(By.XPATH, '//*[@id="Booking_CheckInToDate"]')
    departure_date.clear()
    departure_date.send_keys(departure)

    se_driver.execute_script("document.querySelector('#Booking_NightCount')."
                             "setAttribute('value', '{}')".format(nights))
    se_driver.execute_script("document.querySelector('#Booking_Occupancy')."
                             "setAttribute('value', '{}')".format(occupancy))

    se_driver.implicitly_wait(5)

    se_driver.find_element(By.XPATH, '//*[@id="submit"]').submit()


def print_avaliability(se_driver):
    """
    Check for room availability, if there is a match return a list of all available bookings

    :param se_driver: valid selenium driver
    :precondition se_driver: webdriver must be accessible by computer
    :postcondition: if there is room availability will generate a list of available bookings
    :return: list of tuples containing available bookings
    """
    avalability = se_driver.find_elements(By.CLASS_NAME, 'td-Checkin-Checkout')
    avaliable_rooms = []
    for checkin, checkout in zip(*[iter(avalability)] * 2):
        avaliable_rooms.append(('checking: {0}, checkout: {1}'.format(checkin.text, checkout.text)))

    return avaliable_rooms


def main(url):
    driver = webdriver.Chrome()
    driver.get(url)

    login(driver)
    page_navigation(driver)

    try:
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '/html/body/div[11]/div[1]/button')))
    except:
        pass
    else:
        driver.find_element(By.XPATH, '/html/body/div[11]/div[1]/button').click()

    check_for_bookings(driver, 'Embarc® Whistler', '01-May-2023', '08-May-2023', '2', '3')
    print(print_avaliability(driver))


if __name__ == '__main__':
    main('https://member.embarcresorts.com/')
