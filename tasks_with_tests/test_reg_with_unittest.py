import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()


class TestRegistration(unittest.TestCase):
    def test_first_page(self):
        try:
            browser.get(link1)
            browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Ivan')
            browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Ivanov')
            browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('ivan@ivanov.com')
            button = browser.find_element(By.CSS_SELECTOR, ".btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            time.sleep(10)
            browser.quit()

    def test_second_page(self):
        try:
            browser.get(link2)
            browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Ivan')
            browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Ivanov')
            browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('ivan@ivanov.com')
            button = browser.find_element(By.CSS_SELECTOR, ".btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            time.sleep(10)
            browser.quit()
