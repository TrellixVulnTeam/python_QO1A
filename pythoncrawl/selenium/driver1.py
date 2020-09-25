# 웹 드라이버 테스트
from selenium import webdriver
import time

browser = webdriver.Chrome("d:/webdriver/chromedriver.exe")
browser.implicitly_wait(3)  # 내부 대기시간_필수사항 아님/환경이 다르기 때문에 사이트 들어가기위한 대기시간을 주는 것
browser.maximize_window()

browser.get("https://www.daum.net")
print(browser.current_url)
print(browser.title)

time.sleep(3) # browser.implicitly_wait(3)와 같은 개념

browser.quit()
