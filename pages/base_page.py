import math

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import BasePageLocators


class BasePage:
    TIMEOUT = 4

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(self.TIMEOUT)

    def open(self):
        self.browser.get(url=self.url)

    def go_to_login_page(self):
        self.should_be_login_link()
        link = self.get_element(locator=BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        self.should_be_basket_link()
        basket_button = self.get_element(locator=BasePageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(locator=BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(locator=BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_basket_link(self):
        assert self.is_element_present(locator=BasePageLocators.BASKET_BUTTON), "Basket button is not presented"

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, locator, timeout=TIMEOUT):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator, timeout=TIMEOUT):
        try:
            WebDriverWait(self.browser, timeout, 1, [TimeoutException]). \
                until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
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
