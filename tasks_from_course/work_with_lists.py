from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    def sum(x, y):
        res = int(x) + int(y)
        return str(res)

    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_num = browser.find_element(By.ID, "num1")
    x = first_num.text

    second_num = browser.find_element(By.ID, "num2")
    y = second_num.text

    value = sum(x, y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()




finally:
    time.sleep(20)
    browser.quit()