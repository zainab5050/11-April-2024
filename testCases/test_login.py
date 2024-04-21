import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from PageObjects.login_page import loginPage
from PageObjects.student_Info_menu_page import student_Info
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class Test_001_login:
    gender_xpath = "//select[@name='gender']"
    gender_options_xpath = "//select[@name='gender']//option"
    category_drpdown_xpath = "//select[@id='category_id']"
    category_drpdown_options_xpath = "//select[@id='category_id']//option"
    email_xpath = "//input[@id='email']"
    admission_date_xpath = "//input[@id='admission_date']"
    student_photo_xpath = "//form[@id='form1']//div//div[@class='bozero']//div//input[@id='file']"
    route_list_xpath = "//select[@id='vehroute_id']"
    route_list_options_xpath = "//select[@id='vehroute_id']"
    pickup_point_xpath = "//select[@id='pickup_point']"
    pickup_point_options_xpath = "//select[@id='pickup_point']"
    feeMonth_xpath = "//button[normalize-space()='Select Month']"
    feeMonth_options_xpath = "//div[@class='card-sidebar']//ul//li"
    class4_General_rb_xpath = "//input[@value='46']"
    plus_sign = "//tbody/tr[11]/td[1]/div[1]/div[1]/div[1]/h6[1]/a[1]"
    lastname_txtfield_xpath = "//input[@id='lastname']"
    calendar_DOB_element_xpath = "//input[@id='dob']"

    gardiann = "//input[@value='mother']"
    gardiann_name_xpath = "//input[@id='guardian_name']"
    gardiann_phone_xpath = "//input[@id='guardian_phone']"
    save_button = "//button[@id='addloader']"

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

    def test_create_student(self, setup, test_login):
        driver = setup
        act_title = driver.title
        print(act_title)

        student_Info_obj = student_Info(driver)
        time.sleep(2)
        student_Info_obj.clickStuInfo_menu()

        student_Info_obj.wait_for_element_clickable(self,
                                                    "//ul[@class='treeview-menu']//a[normalize-space()='Student Admission']",
                                                    10)
        student_Info_obj.clickStuAdmission_menu()
        student_Info_obj.wait_presence_of_element_located(self, "//input[@id='admission_no']", 10)
        student_Info_obj.setAdmissionNo_textfld("122")
        student_Info_obj.setroll_no("110")
        student_Info_obj.select_ClassID("Class 4")
        student_Info_obj.setSection("A")
        student_Info_obj.setFirstName_textfld("zeenat")
        student_Info_obj.set_txtField_Value_DF("Khan", self.lastname_txtfield_xpath)
        student_Info_obj.set_dropdown_option_DF(self.gender_xpath, self.gender_options_xpath, "Female")
        student_Info_obj.setCalander_Date_DF(self.calendar_DOB_element_xpath, "August 2018", "16")
        student_Info_obj.set_dropdown_option_DF(self.category_drpdown_xpath, self.category_drpdown_options_xpath, "OBC")
        student_Info_obj.set_txtField_Value_DF("zainab@gmail.com", self.email_xpath)
        student_Info_obj.setCalander_Date_DF(self.admission_date_xpath, "March 2024", "17")
        student_Info_obj.set_txtField_Value_DF("D://upload file//student.avif", self.student_photo_xpath)
        student_Info_obj.select_option_by_text_DF(self.route_list_xpath, self.route_list_options_xpath, "VH5645")
        time.sleep(2)
        student_Info_obj.select_option_by_text_DF(self.pickup_point_xpath, self.pickup_point_options_xpath, "Manhattan")
        # student_Info_obj.set_dropdown_option_DF(self.feeMonth_xpath, self.feeMonth_options_xpath, "July")
        student_Info_obj.click_DF(self.gardiann)
        student_Info_obj.set_txtField_Value_DF("gul", self.gardiann_name_xpath)
        student_Info_obj.set_txtField_Value_DF("1234567890", self.gardiann_phone_xpath)
        student_Info_obj.click_DF(self.save_button)
