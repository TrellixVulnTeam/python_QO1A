# naver 접속 후 검색어 넣고 페이지 이동하는 코드
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("d:/webdriver/chromedriver.exe")
browser.implicitly_wait(3)
browser.get("http://www.naver.com")

# print(browser.title)

assert "NAVER" in browser.title
element = browser.find_element_by_name("query")
element.clear()
element.send_keys("TOEIC")
element.send_keys(Keys.RETURN)

time.sleep(3)
browser.quit()