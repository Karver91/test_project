from pages.login_page import LoginPage


def test_guest_should_see_login_page(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.should_be_login_page()
