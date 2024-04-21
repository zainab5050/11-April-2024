from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http:\\www.google.com")
# driver.save_screenshot("D:\\zzz\SS.png")
driver.get_screenshot_as_file("C:\\auto\\april\\SS\\test1.png")