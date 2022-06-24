from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("input#username").send_keys("xx")
driver.find_element_by_css_selector("input#username").clear()
driver.find_element_by_partial_link_text("Use Custom Domain").click()
driver.find_element_by_xpath("//button[text()='Back']").click()