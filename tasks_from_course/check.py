import unittest
from selenium import webdriver
import time

class TestMePlease(unittest.TestCase):

    def test_1(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1024, 762)

        driver.get("https://www.google.com/")
        time.sleep(7)

        driver.close()

    if __name__ == "__main__":
        unittest.main

