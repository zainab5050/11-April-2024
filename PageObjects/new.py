import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
fp.set_preference("browser.download.manager.showwhenstarting", False)
fp.set_preference("browser.download.folderList", 2)  # 0 for desktop, 1 for downloads, 2 for custom location
fp.set_preference("browser.download.dir", "D:\\zzainab")
fp.set_preference("pdfjs.disabled", True)

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
service_obj = Service("C:\\Users\\LENEVO\\.cache\\selenium\\geckodriver\\win64\\0.34.0\\geckodriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//textarea[@id='pdfbox']").send_keys("zzzz")
driver.find_element(By.XPATH, "//button[@id='createPdf']").click()
driver.find_element(By.XPATH, "//a[@id='pdf-link-to-download']").click()
time.sleep(5)

downloaded_file_path = os.path.join("D:\\zzainab", "Sample.pdf")
if os.path.exists(downloaded_file_path):
    print("File downloaded successfully to:", downloaded_file_path)
else:
    print("File not found in the specified directory.")
driver.quit()
