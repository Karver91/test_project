from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service as ChromeService, Service as ChromiumService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager
from webdriver_manager.opera import OperaDriverManager

from enums import BrowserName


class Settings:
    @staticmethod
    def get_web_driver(name: BrowserName, options=None):
        """Принимает имя браузера, возвращает его веб-драйвер"""
        match name:
            case BrowserName.FIREFOX:
                return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

                # если firefox установлен через snap:
                # return webdriver.Firefox(
                #     service=FirefoxService(executable_path='/snap/bin/firefox.geckodriver'), options=options
                # )
            case BrowserName.CHROME:
                return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            case BrowserName.CHROMIUM:
                return webdriver.Chrome(
                    service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
                    options=options
                )
            case BrowserName.EDGE:
                return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
            case BrowserName.IE:
                return webdriver.Ie(service=IEService(IEDriverManager().install()), options=options)
            case BrowserName.OPERA:
                webdriver_service = service.Service(OperaDriverManager().install())
                webdriver_service.start()

                # options = webdriver.ChromeOptions()
                # options.add_experimental_option('w3c', True)

                # Если браузер Opera установлен в папке, отличной от C:/Program Files или C:/Program Files (x86)
                # в Windows и /usr/bin/opera для всех вариантов Unix и Mac, используйте приведенный ниже код
                # options = webdriver.ChromeOptions()
                # options.binary_location = "path/to/opera.exe"

                return webdriver.Remote(webdriver_service.service_url, options=options)
            case _:
                raise ValueError("Неверно указано имя браузера")


settings = Settings()
