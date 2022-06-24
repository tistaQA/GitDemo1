from selenium import webdriver
import time

#driver = webdriver.Firefox(executable_path="D:\\geckodriver.exe")
driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.find_element_by_id("fromCity").click()
time.sleep(2.5)
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
time.sleep(10)
i = driver.find_elements_by_css_selector("p[class*='blackText']")
for city in i:

    if city.text == "Dehradun, India":
        city.click()
        break

time.sleep(2.5)
driver.find_element_by_css_selector("input[placeholder='To']").send_keys("ban")

items= driver.find_elements_by_css_selector("p[class*='blackText']")

for item in items:
    if item.text == "Bangkok, Thailand":
        item.click()
        break






