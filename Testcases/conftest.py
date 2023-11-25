import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.core.os_manager import ChromeType


@pytest.fixture(autouse=True)
def setup(request, browser):
    global driver
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)

    if browser == "chrome":
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "brave":
        driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())

    driver.get("https://yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


    # options = webdriver.ChromeOptions()
    # prefs = {"profile.default_content_setting_values.notifications": 2}
    # options.add_experimental_option("prefs", prefs)
    # options.add_experimental_option("useAutomationExtension", False)
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    # #wait = WebDriverWait(driver, 30)
    # driver.get("https://www.yatra.com")
    # driver.maximize_window()
    # #request.cls.wait = wait
    # request.cls.driver = driver
    # yield
    #
