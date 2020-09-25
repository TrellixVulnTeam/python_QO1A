from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 다나와 사이트에서 자동 로그인하기
driver = webdriver.Chrome("d:/webdriver/chromedriver.exe")
driver.get("http://www.danawa.com/")
driver.maximize_window()
driver.implicitly_wait(3)

assert "다나와" in driver.title

# 로그인 버튼 클릭
driver.find_element_by_css_selector("li.my_page_service > a").click()

# 아이디 란에 입력
id_area = driver.find_element_by_id("danawa-member-login-input-id")
id_area.clear()
id_area.send_keys("hee12321")

# 비밀번호 란에 입력
pw_area = driver.find_element_by_id("danawa-member-login-input-pwd")
pw_area.clear()
pw_area.send_keys("wogml123*")

# 로그인 버튼 클릭하기/비밀번호란에서 엔터해도됨
# pw_area.send_keys(Keys.RETURN)
driver.find_element_by_id("danawa-member-login-loginButton").click()

time.sleep(3)
driver.quit()
