import sys

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Type in browser type")
    parser.addoption("--executor", action="store", default="standalone", help="For selenium grid.")
    parser.addoption("--url", action="store", default="http://the-internet.herokuapp.com", help="url")




@pytest.fixture(scope="module")
def browser(request):
    browser = request.config.getoption("--browser")

    if browser.lower() == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager(cache_valid_range=0).install())
    elif browser.lower() == 'internet explorer':
        driver = webdriver.Ie(IEDriverManager().install())
    elif browser.lower() == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser.lower() == 'opera':
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        print("Browser Error. Please select a correct browser type")
        sys.exit(0)
    driver.implicitly_wait(10)
    driver.maximize_window()

    def kill_browser():
        print(">>> conftest fixture teardown: chrome (scope:module)")
        driver.save_screenshot("report/last_screenshot.png")
        print("closing")
        driver.close()
        print("<<< conftest fixture teardown: chrome (scope:module)")

    request.addfinalizer(kill_browser)
    return driver