from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class loginPage:
    admin_button_xpath = "//a[contains(text(),'Admin')]"
    username_field_xpath = "//input[@id='form-username']"
    submit_button_xpath = "//button[@type='submit']"
    logout_option_xpath = "//img[@class='topuser-image']"
    logout_icon_xpath = "//a[@class='pull-right']"

    username = "//input[@id='username']"
    password_xpath = "//input[@id='password']"
    submit_button = "//button[@id='submit']"
    logout_xpath = ("//a[@class='wp-block-button__link has-text-color has-background "
                    "has-very-dark-gray-background-color']")

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.username).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_submitt(self):
        self.driver.find_element(By.XPATH, self.submit_button).click()

    def click_logouttt(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()

    def clickAdminButton(self):
        self.driver.find_element(By.XPATH, self.admin_button_xpath).click()

    def clickSignInButton(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def click_Logout(self):
        self.driver.find_element(By.XPATH, self.logout_option_xpath).click()
        self.driver.find_element(By.XPATH, self.logout_icon_xpath).click()

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
