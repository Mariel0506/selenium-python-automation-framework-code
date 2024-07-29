import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture(scope="class")
def setup(request, browser, url):
    # Initialize options based on browser
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        options.add_experimental_option(
            "prefs", {"profile.default_content_setting_values.notifications": 1}
        )
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        # Firefox does not use the same experimental options as Chrome
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--guest")
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        options.add_experimental_option(
            "prefs", {"profile.default_content_setting_values.notifications": 1}
        )
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # driver.get("https://www.yatra.com")
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


# run command: pytest --browser chrome --url https://www.yatra.com