from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome("d:/webdriver/chromedriver.exe", options=options)

driver.get("https://news.v.daum.net/v/20200921150226267")

# 타이틀 가져오기
# //*[@id="cSub"]/div/h3
# //: 문서의 처음부터, * : 사이에 뭐가와도 상관없고, id가 cSub인걸 찾아서, 그 밑에 div 밑에 h3

print(driver.find_element_by_xpath("//*[@id='cSub']/div/h3").text)

driver.quit()
