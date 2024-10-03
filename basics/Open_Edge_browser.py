from selenium import webdriver
from selenium.webdriver.chrome.options import Options


driver = webdriver.Edge()
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
print(driver.title)
print(driver.current_url)
driver.close()
