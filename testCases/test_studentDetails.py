import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from PageObjects.login_page import loginPage
from PageObjects.student_Info_menu_page import student_Info
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class ActionChain:
    pass


class Test_002_student_Details:
    class_drpdown_xpath = "//select[@id='class_id']"
    class_drpdown_options_xpath = "//select[@id='class_id']//option"
    section_dropdown_xpath = "//select[@id='section_id']"
    section_dropdown_options_xpath = "//select[@id='section_id']//option"
    search_by_keyword_txtfield_xpath = "//button[@value='search_filter']"
    student_detail_xpath = "//li[@class='active']//a[normalize-space()='Student Details']"
    student_category_xpath = "Student Categories"
    category_xpath = "//input[@id='category']"
    save_button_xpath = "//button[@class='btn btn-info pull-right']"
    bulk_delete_menu_xpath = "Bulk Delete"
    select_all_xpath = "//input[@name='checkAll']"
    delete_button_xpath = "//button[@id='load']"
    @pytest.fixture()
    def test_login(self, setup):
        driver = setup
        driver.get(Readconfig.getApplicationURL())
        driver.maximize_window()

        # Assuming loginPage.lp is a class attribute, initialize it before using
        loginPage.lp = loginPage(driver)
        loginPage.lp.clickAdminButton()
        loginPage.lp.clickSignInButton()
        time.sleep(4)

    @pytest.mark.skip(reason=None)
    def test_search_student(self, setup, test_login):
        driver = setup
        title = driver.title
        driver.implicitly_wait(10)
        print(title)
        student_Info.obj = student_Info(driver)
        student_Info.obj.clickStuInfo_menu()
        time.sleep(2)
        student_Info.obj.click_DF(self.student_detail_xpath)
        student_Info.obj.set_dropdown_option_DF(self.class_drpdown_xpath, self.class_drpdown_options_xpath,
                                                "Class 4")

        student_Info.obj.set_dropdown_option_DF(self.section_dropdown_xpath, self.section_dropdown_options_xpath, "A")
        # student_Info.obj.set_txtField_Value_DF("Scarlett Kennedy", self.search_by_keyword_txtfield_xpath)
        student_Info.obj.click_DF(self.search_by_keyword_txtfield_xpath)
        time.sleep(2)
        xx = len(driver.find_elements(By.XPATH, "//tbody//tr"))
        for row in range(1, xx + 1):
            for col in (1, 9):
                records = driver.find_elements(By.XPATH, ".//tr[" + str(row) + "]//td[" + str(col) + "]")
                for i in records:
                    print(i.text)

    @pytest.mark.skip()
    def test_student_category(self, setup, test_login):
        driver = setup
        student_Info.obj = student_Info(driver)
        student_Info.obj.clickStuInfo_menu()
        time.sleep(2)
        student_Info.obj.click_by_partialLink_DF(self.student_category_xpath)
        time.sleep(2)
        student_Info.obj.set_txtField_Value_DF("zainab category", self.category_xpath)
        student_Info.obj.click_DF(self.save_button_xpath)
        time.sleep(1)
        records = driver.find_elements(By.XPATH, "//tbody//tr")
        for i in records:
            print(i.text)

    def test_bulk_delete(self, setup, test_login):
        driver = setup
        student_Info.obj = student_Info(driver)
        student_Info.obj.clickStuInfo_menu()
        time.sleep(3)
        student_Info.obj.click_by_partialLink_DF(self.bulk_delete_menu_xpath)
        student_Info.obj.set_dropdown_option_DF(self.class_drpdown_xpath, self.class_drpdown_options_xpath, "Class 4")
        time.sleep(2)
        student_Info.obj.set_dropdown_option_DF(self.section_dropdown_xpath, self.section_dropdown_options_xpath, "A")
        student_Info.obj.click_DF(self.search_by_keyword_txtfield_xpath)
        time.sleep(2)
        student_Info.obj.click_DF(self.delete_button_xpath)
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        alert.accept()
        student_Info.obj.click_DF(self.select_all_xpath)
        student_Info.obj.click_DF(self.delete_button_xpath)


