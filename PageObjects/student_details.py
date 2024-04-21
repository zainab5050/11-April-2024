import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class student_details_page:


    def __init__(self, driver):
        self.driver = driver


