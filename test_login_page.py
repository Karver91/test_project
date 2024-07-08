from pages.login_page import LoginPage

LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_guest_should_see_login_page(browser):
    login_page = LoginPage(browser, LINK)
    login_page.open()
    login_page.should_be_login_page()
