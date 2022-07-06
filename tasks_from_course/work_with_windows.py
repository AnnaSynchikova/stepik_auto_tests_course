from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import sin, log

try:
    #open the link
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # push the button
    browser.find_element(By.CSS_SELECTOR, ".btn").click()

    # switch to the new window
    browser.switch_to.window(browser.window_handles[1])

    # get x value
    val = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(val.text)

    # get value of function
    func_val = log(abs(12*sin(x)))

    # send value to forms and push the submit button
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(func_val)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep(10)
    browser.quit()