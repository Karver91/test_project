import pytest
from selenium import webdriver

from config import settings
from enums import BrowserName


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help='Select your browser language. For example: en, ru, fr')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    match browser_name:
        case BrowserName.CHROME.value:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            print(f"\nstart {browser_name} browser for test..")
            browser = settings.get_web_driver(name=BrowserName.CHROME, options=options)
        case BrowserName.FIREFOX.value:
            print(f"\nstart {browser_name} browser for test..")
            options = webdriver.FirefoxOptions()
            options.set_preference(
                "intl.accept_languages", user_language
            )
            browser = settings.get_web_driver(name=BrowserName.FIREFOX, options=options)
        case _:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
