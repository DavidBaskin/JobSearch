import time

from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store",
                     default="chrome", help="Type in browser name e.g. chrome OR firefox")


@pytest.fixture(scope='class')
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome()

    elif browser == 'firefox':
        driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.close()
    driver.quit()
    print("Test Completed")
