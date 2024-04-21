from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()

# # get all cokkies
# cookies = driver.get_cookies()
# for c in cookies:
#     print(c.get('name'), ":", c.get("value"))
#
# # Add cookie
# cookie = {'name': 'Mycookie', 'value': '123zzz'}
# driver.add_cookie(cookie)
# cookies = driver.get_cookies()
# print(len(cookies))
# print("my cookie is:", cookie)

# del cookies
driver.delete_all_cookies()
cook = driver.get_cookies()
print(len(cook))

