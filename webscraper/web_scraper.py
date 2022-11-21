from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
import string
import json


def web_scraper(web_page_source):
    print_out = BeautifulSoup(web_page_source, 'html.parser')  # creates page as bs4 object

    gym_titles = print_out.find_all('a', {'class': 'css-1m051bw'})
    descriptions = print_out.find_all('p', {'class': 'css-16lklrv'})
    # rating = print_out.find_all('span', {'class': ' css-gutk1c'})
    images = print_out.find_all('img')

    my_doc = {}

    for (gyms, description, img) in zip(gym_titles, descriptions, images):
        key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=22))
        my_doc[key] = {}
        my_doc[key]['gym name'] = str(gyms.text)
        my_doc[key]['description'] = str(description.text)
        my_doc[key]['image'] = str(img['src'])
        my_doc[key]['rating'] = random.randint(1, 5)
        my_doc[key]['distance'] = random.randint(1, 20)

    try:
        with open('gyms.json', 'a') as file_object:
            json.dump(my_doc, file_object)
    except FileNotFoundError:
        with open('gyms.json', 'w') as file_object:
            json.dump(my_doc, file_object)


def web_page_turner(url):
    browser = webdriver.Chrome()
    browser.get(url)

    try:
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH,
                                                             '//*[@id="main-content"]/div/ul/li[21]/div/div[1]/div/div[11]/span/a/span')))  # name of gym name class
    except:
        print('failed')
    else:
        button = browser.find_element(By.XPATH,
                                      '//*[@id="main-content"]/div/ul/li[21]/div/div[1]/div/div[11]/span/a/span')
        button.click()
        return str(browser.current_url)
    finally:
        browser.quit()


def main(web_page):
    # selenium
    browser = webdriver.Chrome()
    browser.get(web_page)
    webpage = browser.page_source

    try:
        # tells selenium to wait until elements exist
        WebDriverWait(browser, 120).until(expected_conditions.presence_of_element_located
                                          ((By.CLASS_NAME, "css-1m051bw")))  # name of gym name class
    except:  # required for try statement
        print('failed')
    else:
        count = 0
        while count < 5:
            web_scraper(webpage)
            main(web_page_turner(web_page))
            count += 1
    finally:
        browser.quit()


if __name__ == '__main__':
    main('https://www.yelp.ca/search?cflt=gyms&find_loc=Coquitlam%2C+BC')
