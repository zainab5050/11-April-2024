from selenium.webdriver.common.by import By


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
