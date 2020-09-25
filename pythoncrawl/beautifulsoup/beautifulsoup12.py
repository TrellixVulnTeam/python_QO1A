# 네이버 주식 인기검색종목 가져오기
import requests
from bs4 import BeautifulSoup

res = requests.get("https://finance.naver.com/")
soup = BeautifulSoup(res.content, "html.parser")

title = soup.find("h3", class_="h_popular")
print(title.string)

# div.aside_area.aside_popular > table > tbody > tr:nth-child(1)
popular_contents = soup.select("div.aside_area.aside_popular > table > tbody > tr")
# print(popular_contents)
for tr in popular_contents:
    # 종목명
    stock_name = tr.select_one("a").get_text()
    # 현재가격
    stock_price = tr.select_one("td").get_text()
    print(stock_name, stock_price)

print()

# 네이버 주식 해외 증시 가져오기
title2 = soup.find("h3", class_="h_stock")
print(title2.string)

# div.aside_area.aside_stock > table
stock_contents = soup.select("div.aside_area.aside_stock > table > tbody > tr")
# print(stock_contents)
for tr in stock_contents:
    # 해외 증시
    stock_name = tr.select_one("a").get_text()
    # 해외 증시 지수
    stock_price = tr.select_one("td").get_text()
    # 증감
    stock_up_down = tr.select_one("td:nth-child(3)").get_text()
    print(stock_name, stock_price, stock_up_down)
