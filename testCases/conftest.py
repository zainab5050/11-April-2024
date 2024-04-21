import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.login_page import loginPage
from utilities.readProperties import Readconfig
from selenium.webdriver.support import expected_conditions as EC, wait


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='class')
def test_login(setup):
    driver = setup
    driver.get(Readconfig.getApplicationURL())
    driver.maximize_window()

    # Assuming loginPage.lp is a class attribute, initialize it before using
    loginPage.lp = loginPage(driver)
    loginPage.lp.clickAdminButton()
    loginPage.lp.clickSignInButton()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.url_contains('dashboard'))
    return driver


@pytest.fixture()
def setupp():
    driver = webdriver.Chrome()
    return driver
