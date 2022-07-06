from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # open the link
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # send values to the forms
    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys("name")
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys("lastname")
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys("email")

    # load file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)

    # push the "submit" button
    browser.find_element(By.CSS_SELECTOR, '.btn').click()


finally:
    time.sleep(10)
    browser.quit()



