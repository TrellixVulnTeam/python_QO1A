from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("d:/webdriver/chromedriver.exe")

driver.get("https://www.facebook.com/")

# id xpath
email_path = "//*[@id='email']"

# password xpath
pass_path = "//*[@id='pass']"

email_path = driver.find_element_by_xpath(email_path)
pass_path = driver.find_element_by_xpath(pass_path)

# 로그인 시도
email_path.clear()
email_path.send_keys("")
pass_path.clear()
pass_path.send_keys("")
pass_path.send_keys(Keys.RETURN)

driver.quit()
