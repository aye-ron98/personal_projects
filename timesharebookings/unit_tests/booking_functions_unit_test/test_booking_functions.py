from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_send_username(self):
        driver = self.driver
        driver.get('https://member.embarcresorts.com/')

        username = driver.find_element(By.XPATH, '//*[@id="Username"]')
        username.send_keys('test')

        assert_success = driver.find_element(By.XPATH, '//*[@id="Username"]')
        assert 'test' in assert_success.text

    def tearDown(self):
        self.driver.close()
