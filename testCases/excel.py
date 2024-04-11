import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from PageObjects.login_page import loginPage
from PageObjects.student_Info_menu_page import student_Info
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from utilities import xl_util


class Test_002_xlLogin:
    baseURL = Readconfig.getApplicationURL()
    path = ".//testData/Book1.xlsx"
    logger = LogGen.loggen()

    def test_browse_xl_login(self, setup):
        self.driver = setup
        self.logger.info("********** start Test_002_xlLogin *********")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.rows = xl_util.getRowCount(self.path, 'Sheet1')
        print(self.rows)

        lst_status = []
        for r in range(2, self.rows + 1):
            self.user = xl_util.readData(self.path, 'Sheet1', r, 1)
            self.password = xl_util.readData(self.path, 'Sheet1', r, 2)
            self.exp = xl_util.readData(self.path, 'Sheet1', r, 3)

            self.lp = loginPage(self.driver)
            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.click_submitt()
            time.sleep(5)

            actual_title = self.driver.title
            print(actual_title)
            exp_title = "Logged In Successfully | Practice Test Automation"

            if actual_title == exp_title:
                if self.exp == "pass":
                    print("pass")
                    self.lp.click_logouttt()
                    lst_status.append("pass")
                elif self.exp == "fail":
                    self.lp.click_logouttt()
                    print("fail")
                    lst_status.append("fail")
            elif actual_title != exp_title:
                if self.exp == "pass":
                    print("fail")
                    lst_status.append("Fail")
                elif self.exp == "fail":
                    print("pass")
                    lst_status.append("pass")

        if "fail" not in lst_status:
            self.logger.info("*****Login DDT test Passed")
            self.driver.close()
        else:
            self.logger.info("**** FULL excell Login DDT test is Failed****")
            self.driver.close()
            assert False

        self.logger.info("###### END ######")
