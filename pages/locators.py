from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "basket-mini")]/child::span[@class="btn-group"]/child::a[contains(@class, "btn")]'
    )
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass


class BasketPageLocators:
    BASKET_PRODUCT_FORM = (
        By.XPATH,
        '//div[@class="content"]/child::div[@id="content_inner"]/form[@id="basket_formset"]'
    )
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//div[@class="content"]/child::div[@id="content_inner"]/p')


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
