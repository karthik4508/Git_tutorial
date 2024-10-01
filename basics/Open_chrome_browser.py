from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome()
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
print(driver.title)
driver.close()