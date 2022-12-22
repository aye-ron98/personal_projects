from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import booking_functions as bookings


def main(url):
    driver = webdriver.Chrome()
    driver.get(url)

    bookings.login(driver)
    bookings.page_navigation(driver)

    try:
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '/html/body/div[11]/div[1]/button')))
    except:
        pass
    else:
        driver.find_element(By.XPATH, '/html/body/div[11]/div[1]/button').click()

    bookings.check_for_bookings(driver, 'Embarc® Whistler', '01-May-2023', '08-May-2023', '2', '3')
    print(bookings.print_avaliability(driver))


if __name__ == '__main__':
    main('https://member.embarcresorts.com/')
