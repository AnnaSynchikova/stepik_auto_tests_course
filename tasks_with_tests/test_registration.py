from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()