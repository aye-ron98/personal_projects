from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


# def open_booking_site(site):
#     """
#     Open the embarc website and return a working driver link
#
#     :param site: valid URL to the embarc website
#     :precondition site: website URL as a string
#     :postcondition: a working driver link program will run on
#     :return: site drive link
#     """


def main(url):
    driver = webdriver.Chrome()
    driver.get(url)

    username = driver.find_element(By.XPATH, '//*[@id="Username"]')
    username.send_keys('erwinzhang')

    password = driver.find_element(By.XPATH, '//*[@id="Password"]')
    password.send_keys('Safety2021')

    login = driver.find_element(By.XPATH, '//*[@id="page-mobile"]/div[3]/div[2]/div/form/div[3]/div[4]/input')
    login.click()

    clickable = driver.find_element(By.XPATH, '//*[@id="dashboard-content"]/div[2]/div/div[2]/a')
    clickable.click()

    try:
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '/html/body/div[11]/div[1]/button')))
    except:
        pass
    else:
        driver.find_element(By.XPATH, '/html/body/div[11]/div[1]/button').click()

    destination = driver.find_element(By.XPATH, '//*[@id="DestinationSearchTerm"]')
    destination.send_keys('Embarc® Whistler')

    arrival_date = driver.find_element(By.XPATH, '//*[@id="Booking_CheckInFromDate"]')
    arrival_date.clear()
    arrival_date.send_keys('01-Apr-2023')

    departure_date = driver.find_element(By.XPATH, '//*[@id="Booking_CheckInToDate"]')
    departure_date.clear()
    departure_date.send_keys('30-Apr-2023')

    driver.execute_script("document.querySelector('#Booking_NightCount').setAttribute('value', '1')")
    driver.execute_script("document.querySelector('#Booking_Occupancy').setAttribute('value', '3')")

    time.sleep(5)

    # search = driver.find_element(By.ID, 'submit')
    driver.execute_script("document.querySelector('#submit').click()")

    time.sleep(5)

    try:
        avaliability = driver.find_element(By.CSS_SELECTOR, 'table.GridResultsTable')
    except:
        print('sorry there are no bookings avaliable')
    else:
        for row in avaliability.find_element(By.CSS_SELECTOR, 'tr'):
            for cell in row.find_element(By.CSS_SELECTOR, 'td'):
                if cell.getAttribute('class') == 'td-Checkin-Checkout':
                    print(cell.text())


if __name__ == '__main__':
    main('https://member.embarcresorts.com/')
