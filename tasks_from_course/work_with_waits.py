from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from math import log, sin


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    browser.find_element(By.CLASS_NAME, "btn-primary").click()

    # get x
    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x.text)

    # get value of function
    func_val = log(abs(12 * sin(x)))

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(func_val)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit()