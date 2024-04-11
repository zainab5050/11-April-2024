from selenium.webdriver.common.by import By


class student_Info:
    student_info_menu_xpath = "//span[normalize-space()='Student Information']"
    student_admission_menu_xpath = "//ul[@class='treeview-menu menu-Admission']"
    AdmissionNo_txtfld_xpath = "//input[@id='admission_no']"
    classID_dropdown_xpath = "//select[@id='class_id']"

    def __init__(self, driver):
        self.driver = driver

    def clickStuInfo_menu(self):
        self.driver.find_element(By.XPATH, self.student_info_menu_xpath).click()

    def clickStuAdmission_menu(self):
        self.driver.find_element(By.XPATH, self.student_admission_menu_xpath).click()

    def setAdmissionNo_textfld(self, addmisionNo):
        self.driver.find_element(By.XPATH, self.setAdmissionNo_textfld).clear()
        self.driver.find_element(By.XPATH, self.setAdmissionNo_textfld).send_keys(addmisionNo)

    def click_ClassID(self):
        self.driver.find_element(By.XPATH, self.click_ClassID).click()
