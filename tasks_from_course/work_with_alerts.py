from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import sin, log

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # push the button
    browser.find_element(By.CSS_SELECTOR, ".btn").click()

    # accept alert
    browser.switch_to.alert.accept()

    # get x
    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x.text)

    # get value of function
    func_val = log(abs(12*sin(x)))

    # send value to forms and push the submit button
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(func_val)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep(10)
    browser.quit()