import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def select_option_by_text(dropdown_element, option_text):
    select = Select(dropdown_element)
    select.select_by_visible_text(option_text)


class student_Info:
    student_info_menu_xpath = "//span[normalize-space()='Student Information']"
    student_admission_menu_xpath = "//ul[@class='treeview-menu']//a[normalize-space()='Student Admission']"
    admissionNo_txtfld_xpath = "//input[@id='admission_no']"
    classID_dropdown_xpath = "//select[@id='class_id']"
    classId_options_xpath = "//select[@id='class_id']//option"
    section_dd_xpath = "//select[@id='section_id']"
    section_options_xpath = "//select[@id='section_id']//option"
    rollno_field_xpath = "//input[@id='roll_no']"
    firstName_txtfield_xpath = "//input[@id='firstname']"

    def __init__(self, driver):
        self.driver = driver

    def clickStuInfo_menu(self):
        self.driver.find_element(By.XPATH, self.student_info_menu_xpath).click()

    def StuAdmission_menu_locator(self):
        self.driver.find_element(By.XPATH, self.student_admission_menu_xpath)

    def clickStuAdmission_menu(self):
        element = self.driver.find_element(By.XPATH, self.student_admission_menu_xpath)
        self.driver.execute_script("arguments[0].click();", element)

    def setAdmissionNo_textfld(self, addmisionNo):
        self.driver.find_element(By.XPATH, self.admissionNo_txtfld_xpath).clear()
        self.driver.find_element(By.XPATH, self.admissionNo_txtfld_xpath).send_keys(addmisionNo)

    def setroll_no(self, rollno):
        self.driver.find_element(By.XPATH, self.rollno_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.rollno_field_xpath).send_keys(rollno)

    def select_ClassID(self, DD_option):
        dd_element = self.driver.find_element(By.XPATH, self.classID_dropdown_xpath)
        self.driver.execute_script("arguments[0].click();", dd_element)
        time.sleep(1)
        dd = self.driver.find_elements(By.XPATH, self.classId_options_xpath)
        for i in dd:
            if i.text == DD_option:
                i.click()
                break
        else:
            print("Class Not matched")

    def setSection(self, DD_option):
        dd_element = self.driver.find_element(By.XPATH, self.section_dd_xpath)
        self.driver.execute_script("arguments[0].click();", dd_element)
        time.sleep(1)
        dd = self.driver.find_elements(By.XPATH, self.section_options_xpath)
        for i in dd:
            if i.text == DD_option:
                i.click()
                break
        else:
            print("Section Not matched")

    def setFirstName_textfld(self, firstName):
        self.driver.find_element(By.XPATH, self.firstName_txtfield_xpath).clear()
        self.driver.find_element(By.XPATH, self.firstName_txtfield_xpath).send_keys(firstName)

    def set_txtField_Value_DF(self, value, txt_field_xpath):
        field = self.driver.find_element(By.XPATH, txt_field_xpath)
        field.clear()
        field.send_keys(value)

    def select_option_by_text_DF(self, dropdown_element_xpath, DD_options, requiredOption):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, dropdown_element_xpath)))

        # Click the dropdown element to open options
        dropdown_element = self.driver.find_element(By.XPATH, dropdown_element_xpath)
        dropdown_element.click()

        # Wait for all options to be visible
        all_options = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, DD_options)))

        # Assuming the first element is the select dropdown
        select = Select(dropdown_element)

        # Select the option by visible text
        select.select_by_visible_text(requiredOption)

    # @staticmethod
    def set_dropdown_option_DF(self, dropdown_xpath, options_xpath, option_text):
        dd_element = self.driver.find_element(By.XPATH, dropdown_xpath)
        dd_element.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, options_xpath)))
        options = self.driver.find_elements(By.XPATH, options_xpath)
        for option in options:
            if option.text == option_text:
                option.click()
                return  # Exit the function after clicking the option

        print("Option Not matched")

    def setCalander_Date_DF(self, calander_ele_xpath, required_month, reqDate):
        self.driver.find_element(By.XPATH, calander_ele_xpath).click()
        time.sleep(1)
        while True:
            date = self.driver.find_element(By.XPATH, "//th[@class='datepicker-switch' and contains(text(), ' ')]")
            if required_month in date.text:
                all_dates = self.driver.find_elements(By.XPATH, "//tbody//td[@class='day']")
                for i in all_dates:
                    if i.text == reqDate:
                        i.click()
                        return
            else:
                prev_button = self.driver.find_element(By.XPATH,
                                                       "//div[@class='datepicker-days']//th[@class='prev'][normalize-space()='«']")
                prev_button.click()

    @staticmethod
    def wait_for_element_clickable(self, element_locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.element_to_be_clickable(element_locator))
        except Exception as e:
            print(f" Error : {str(e)}")

    @staticmethod
    def wait_presence_of_element_located(self, element, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located(element))
        except Exception as e:
            print(f" Error : {str(e)}")

    @staticmethod
    def select_DF(self, dropdown_element_xpath, DD_options, requiredOption):
        # Wait for the dropdown element to be visible
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, dropdown_element_xpath)))

        # Click the dropdown element to open options
        element = self.driver.find_element(By.XPATH, dropdown_element_xpath)
        element.click()

        # Wait for all options to be visible
        all_options = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, DD_options)))

        # Check if the dropdown element is a <select> element
        if all_options[0].tag_name == 'select':
            # If it's a <select> element, create a Select object
            select = Select(all_options[0])  # Assuming the first element is the select dropdown

            # Select the option by visible text
            select.select_by_visible_text(requiredOption)
        else:
            # If it's not a <select> element, iterate through options and click the one matching the required text
            for option in all_options:
                if option.text == requiredOption:
                    option.click()
                    break

    def click_DF(self, ele_xpath):
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, ele_xpath)))
        self.driver.find_element(By.XPATH, ele_xpath).click()

    def click_by_partialLink_DF(self, ele_xpath):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, ele_xpath).click()
