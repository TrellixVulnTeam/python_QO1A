# 다음 댓글 가져오기 - 최신순 댓글 가져오기
# Waits : 데이터들이 로드되는 시점의 차이가 존재하는 거
# implicit wait : 웹 페이지 내의 요소를 찾기 위해 web driver가 일정시간 기다리도록 요청 (시간 지정하는 만큼 무작정 기다리는거_조건X)
# explicit wait : web driver가 실행을 계속 하기 전에 특정 조건이 발생할 때까지 기다리는 것 (조건이 충족할 때까지 기다리는거)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

# 웹드라이버 로드
driver = webdriver.Chrome("d:/webdriver/chromedriver.exe")
driver.implicitly_wait(3)

# 정보를 추출할 사이트 접속하기
driver.get("https://news.v.daum.net/v/20200921150226267")

# 최신순 클릭하기

# 최신순 버튼이 보여질 때까지 기다리기
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.cmt_box > ul > li:nth-child(3)")))
# 최신순 버튼 클릭하기
recent_button = driver.find_element_by_css_selector("div.cmt_box > ul > li:nth-child(3)")
recent_button.click()

# 더보기 버튼은 댓글이 없는 경우 생성되지 않는 버튼이기 때문에
# 더보기 버튼이 생긴 경우 클릭하라고 코딩해야함 => explicit wait 사용
loop, count = True, 0

while loop and count < 10:
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.alex_more > button")
            )
        )
        # 생성됐는지 확인
        more_button = driver.find_element_by_css_selector(
            "div.alex_more > button"
        )
        # 실제 클릭
        more_button.click()
        count += 1
        time.sleep(3)
    except TimeoutException as e:
        print(e)
        loop = False

# 댓글 가져오기
comment_lists = driver.find_elements_by_css_selector("ul.list_comment > li > div > p")

for num, comment in enumerate(comment_lists, start=1):
    print("[{}] : {}".format(num, comment.text))

# 종료
driver.quit()
