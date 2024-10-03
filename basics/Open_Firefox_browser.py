from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
print(driver.title)
print(driver.current_url)
driver.close()
