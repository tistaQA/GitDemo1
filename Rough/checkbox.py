import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
items = driver.find_elements_by_css_selector("input[type='checkbox']")
print(len(items))
for i in items:
    #print(i.get_attribute("value"))
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected() # to validate whether the checkboxes are selected or not

time.sleep(5)
radio = driver.find_elements_by_css_selector("input[type='radio']")
radio[2].click()
assert radio[2].is_selected()









