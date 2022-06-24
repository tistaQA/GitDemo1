from selenium import webdriver
# every browser exposes an executable file, Selenium do not have access to invoke directly a browser
# through selenium test, we need to first invoke that executable file which will then invoke the actual browser
#driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe") #driver is an object

driver= webdriver.Firefox(executable_path="D:\\geckodriver.exe")
#get method to hit url on browser
driver.get("https://chromedriver.chromium.org")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
driver.quit()
