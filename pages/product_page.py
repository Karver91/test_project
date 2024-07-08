from pages.base_page import BasePage
from pages.locators import ProductPageLocators, BasePageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_product_to_basket_button()
        self.add_product_is_success()
        self.alerts_displayed_is_success()
        self.alert_product_name_is_correct()
        self.alert_product_price_is_correct()

    def should_be_add_product_to_basket_button(self):
        assert self.is_element_present(locator=ProductPageLocators.ADD_PRODUCT), \
            f'Add_product button is not presented | locator {ProductPageLocators.ADD_PRODUCT}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.PRODUCT_NAME_ALERT), \
            "Success message is presented, but should not be"

    def should_be_element_disappear(self):
        assert self.is_disappeared(ProductPageLocators.PRODUCT_NAME_ALERT), "Element did not disappear"

    def add_product_is_success(self):
        add_product_button = self.get_element(locator=ProductPageLocators.ADD_PRODUCT)
        add_product_button.click()
        self.solve_quiz_and_get_code()

    def alerts_displayed_is_success(self):
        alerts = self.get_multiple_elements(locator=ProductPageLocators.ADD_PRODUCT_SUCCESS_ALERTS)
        assert len(alerts) == 3, "Alerts don't show"

    def alert_product_name_is_correct(self):
        product_name_alert = self.get_element_text(locator=ProductPageLocators.PRODUCT_NAME_ALERT)
        product_name = self.get_element_text(locator=ProductPageLocators.PRODUCT_NAME)
        assert product_name_alert == product_name, "Product name test is failed"

    def alert_product_price_is_correct(self):
        product_price_alert = self.get_element_text(locator=ProductPageLocators.PRICE_ALERT)
        product_price = self.get_element_text(locator=ProductPageLocators.PRODUCT_PRICE)
        assert product_price_alert == product_price, "Product price test is failed"
