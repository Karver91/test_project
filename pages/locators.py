from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "basket-mini")]/child::span[@class="btn-group"]/child::a[contains(@class, "btn")]'
    )
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class BasketPageLocators:
    BASKET_PRODUCT_FORM = (
        By.XPATH,
        '//div[@class="content"]/child::div[@id="content_inner"]/form[@id="basket_formset"]'
    )
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//div[@class="content"]/child::div[@id="content_inner"]/p')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL_FIELD = (
        By.XPATH,
        '//form[@id="register_form"]/descendant::input[@id="id_registration-email"]'
    )
    REGISTRATION_PASS_1_FIELD = (
        By.XPATH,
        '//form[@id="register_form"]/descendant::input[@id="id_registration-password1"]'
    )
    REGISTRATION_PASS_2_FIELD = (
        By.XPATH,
        '//form[@id="register_form"]/descendant::input[@id="id_registration-password2"]'
    )
    REGISTRATION_SUBMIT_BUTTON = (
        By.XPATH,
        '//form[@id="register_form"]/descendant::button[@type="submit"]'
    )


class ProductPageLocators:
    ADD_PRODUCT = (By.XPATH, '//form[@id="add_to_basket_form"]/child::button[@type="submit"]')
    ADD_PRODUCT_SUCCESS_ALERTS = (By.XPATH, '//div[@id="messages"]/descendant::div[@class="alertinner "]')
    PRODUCT_NAME_ALERT = (By.XPATH, '//div[@id="messages"]/descendant::div[@class="alertinner "][1]/strong')
    OFFER_ALERT = (By.XPATH, '//div[@id="messages"]/descendant::div[@class="alertinner "][2]/strong')
    PRICE_ALERT = (By.XPATH, '//div[@id="messages"]/descendant::div[@class="alertinner "]/p/strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main > p.price_color')
