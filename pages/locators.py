from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_PRODUCT = (By.XPATH, '//form[@id="add_to_basket_form"]/child::button[@type="submit"]')
    ADD_PRODUCT_SUCCESS_ALERTS = (By.XPATH, '//div[@id="messages"]/descendant::div[@class="alertinner "]')
    PRODUCT_NAME_ALERT = (By.XPATH, '//div[@id="messages"]/descendant::div[@class="alertinner "][1]/strong')
    OFFER_ALERT = (By.XPATH, '//div[@id="messages"]/descendant::div[@class="alertinner "][2]/strong')
    PRICE_ALERT = (By.XPATH, '//div[@id="messages"]/descendant::div[@class="alertinner "]/p/strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main > p.price_color')

