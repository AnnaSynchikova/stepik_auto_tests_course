from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import sin, log

try:
    #open the link
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    # get x value
    val = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(val.text)

    # get value of function
    func_val = log(abs(12*sin(x)))

    # scroll for a button
    browser.execute_script("window.scrollBy(0, 100)")

    # send value to forms
    browser.find_element(By.ID, 'answer').send_keys(func_val)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep(10)
    browser.quit()
