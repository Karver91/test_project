import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

LINK = "http://selenium1py.pythonanywhere.com"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, LINK)
    main_page.open()
    main_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_no_products_in_basket()
    basket_page.should_be_empty_basket_message()


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, LINK)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, LINK)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser, LINK)
        main_page.open()
        main_page.should_be_login_link()
