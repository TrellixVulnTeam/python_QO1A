from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("d:/webdriver/chromedriver.exe")

browser.get("https://www.daum.net")

assert "Daum" in browser.title

# 접속한 페이지 소스 가져오기
# print(browser.page_source)
# 페이지 소스에서 원하는 요소를 찾기
# 1. selenium 사용 - find~~~ 이름을 갖는 메소드로 처리 가능
# 2. BeautifulSoup 사용

element = browser.find_element_by_name("q")
element.send_keys("아이폰")   # send_keys : 키보드에서 입력할 정보 지정
element.send_keys(Keys.RETURN)

# 검색결과를 가지고 원하는 요소를 파싱


time.sleep(3)
browser.quit()
