from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, '"basket" should be in basket_url'

    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(locator=BasketPageLocators.BASKET_PRODUCT_FORM), \
            'Products are in the cart but should not be'

    def should_be_empty_basket_message(self):
        assert self.is_element_present(locator=BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            'Should be a message that the basket is empty'
