from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

browser = webdriver.Chrome()
browser.get('https://console.firebase.google.com/project/dtc11-8eb98/firestore/data/~2FReviews~2F93rP79bmOzsNf5Cgo2LJ')

input = browser.find_element(By.XPATH, '//*[@id="identifierId"]')
input.send_keys('aron.zhang013@gmail.com')

submit = browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
submit.click()

try:
    WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))  # name of gym name class
except:
    print('failed')

else:
    password = browser.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys('Op3n0p3n')



    print(browser.current_url)

browser.quit()
