import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import unittest


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestStepikPages:
    message = ""

    @pytest.mark.parametrize("url", ["236895",
                                     "236896",
                                     "236897",
                                     "236898",
                                     "236899",
                                     "236903",
                                     "236904",
                                     "236905"])
    def test_feedback(self, browser, url):
        answer = str(math.log(int(time.time())))
        link = f"https://stepik.org/lesson/{url}/step/1"
        browser.implicitly_wait(10)
        browser.get(link)
        browser.find_element(By.TAG_NAME, "textarea").send_keys(answer)
        browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
        result = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        assert result.text == "Correct!", "Wrong text!"

    if __name__ == "__main__":
        unittest.main()
