import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from PageObjects.login_page import loginPage
from PageObjects.student_Info_menu_page import student_Info
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class Test_001_login:
    baseURL = Readconfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_browse(self, setup):
        self.driver = setup
        self.logger.info("********** start test_browse *********")
        self.driver.get(self.baseURL)
        page_title = self.driver.title
        print(page_title)
        if page_title == "Login : Mount Carmel School":
            assert True
            self.driver.close()
            self.logger.info("********** End test_browse *********")
        else:
            self.driver.save_screenshot(".\\SS\\s1.png")
            self.logger.info("********** Error in test_browse *********")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.logger.info("********** start test_login *********")
        self.driver.get(self.baseURL)
        self.lp = loginPage(self.driver)
        self.lp.clickAdminButton()
        time.sleep(3)
        self.lp.clickSignInButton()
        self.logger.info("********** End test_browse *********")
