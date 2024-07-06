import math

from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    TIMEOUT = 5

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(self.TIMEOUT)

    def open(self):
        self.browser.get(url=self.url)

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def get_element(self, locator):
        return self.browser.find_element(*locator)

    def get_multiple_elements(self, locator):
        return self.browser.find_elements(*locator)

    def get_element_text(self, locator):
        return WebDriverWait(
            driver=self.browser, timeout=self.TIMEOUT).until(EC.visibility_of_element_located(locator=locator)).text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
