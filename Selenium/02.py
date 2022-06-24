from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("Rahul Shetty")
driver.find_element_by_class_name("form-check-label").click()
driver.find_element_by_name("email").send_keys("rahul11@yopmail.com")
driver.find_element_by_css_selector("input[name='name']").send_keys("aa")
driver.find_element_by_xpath("//input[@type='submit']").click()

print(driver.find_element_by_css_selector("div[class*='alert-dismissible']").text)

