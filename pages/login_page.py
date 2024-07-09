from time import time

from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email: str, password: str):
        self.should_be_registration_fields()
        self.should_be_register_button()
        email_field = self.get_element(locator=LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        pass_1_field = self.get_element(locator=LoginPageLocators.REGISTRATION_PASS_1_FIELD)
        pass_2_field = self.get_element(locator=LoginPageLocators.REGISTRATION_PASS_2_FIELD)
        submit_button = self.get_element(locator=LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)

        email_field.send_keys(email)
        pass_1_field.send_keys(password)
        pass_2_field.send_keys(password)
        submit_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_registration_fields(self):
        self.should_be_register_email_field()
        self.should_be_register_pass_1_field()
        self.should_be_register_pass_2_field()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, '"login" should be in login_url'

    def should_be_login_form(self):
        assert self.is_element_present(locator=LoginPageLocators.LOGIN_FORM), \
            f'Login form is not presented | locator {LoginPageLocators.LOGIN_FORM}'

    def should_be_register_form(self):
        assert self.is_element_present(locator=LoginPageLocators.REGISTRATION_FORM), \
            f'Login form is not presented | locator {LoginPageLocators.REGISTRATION_FORM}'

    def should_be_register_email_field(self):
        assert self.is_element_present(locator=LoginPageLocators.REGISTRATION_EMAIL_FIELD), \
            f'Registration email field is not presented | locator {LoginPageLocators.REGISTRATION_EMAIL_FIELD}'

    def should_be_register_pass_1_field(self):
        assert self.is_element_present(locator=LoginPageLocators.REGISTRATION_PASS_1_FIELD), \
            f'Registration pass_1 field is not presented | locator {LoginPageLocators.REGISTRATION_PASS_1_FIELD}'

    def should_be_register_pass_2_field(self):
        assert self.is_element_present(locator=LoginPageLocators.REGISTRATION_PASS_2_FIELD), \
            f'Registration pass_2 field is not presented | locator {LoginPageLocators.REGISTRATION_PASS_2_FIELD}'

    def should_be_register_button(self):
        assert self.is_element_present(locator=LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), \
            f'Registration submit button is not presented | locator {LoginPageLocators.REGISTRATION_SUBMIT_BUTTON}'

    @staticmethod
    def get_random_email_passw():
        email = str(time()) + "@fakemail.org"
        passw = str(time())
        return email, passw
