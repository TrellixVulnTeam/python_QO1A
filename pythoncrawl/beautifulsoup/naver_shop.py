import requests
from bs4 import BeautifulSoup
import pprint
import openpyxl

# 엑셀 저장
excel_file = openpyxl.Workbook()
# 기본으로 만들어진 시트 활성화
sheet1 = excel_file.active
# 시트의 열 너비 조절
sheet1.column_dimensions['B'].width = 100
sheet1.column_dimensions['C'].width = 60
# 타이틀 행 삽입
sheet1.append(["순위", "상품명", "주소"])
# 시트 이름 변경
sheet1.title = "샤오미 top100"

# 네이버 오픈API를 이용한 쇼핑 정보 가져오기
url = "https://openapi.naver.com/v1/search/shop.json"

start, num = 1, 0

for idx in range(10):
    # 1, 101, 201, ... 901
    start_num = start + (idx * 100)

    param = {
        "query" : "샤오미",
        "display" : "100",
        "start" : str(start_num)
    }

    headers = {
        "X-Naver-Client-Id" : "KQVDVE9WTmyEUGaxiNGU",
        "X-Naver-Client-Secret" : "bOON5T41cC"
    }

    res = requests.get(url, params=param, headers=headers)
    # print(res.url)
    # pprint.pprint(res.json())
    
    data = res.json()

    if res.status_code == 200:
        for item in data["items"]:
            num += 1
            product_info = [num, item['title'], item['link']]
            sheet1.append(product_info)
    else:
        print("Error", res.status_code)

excel_file.save("./resources/샤오미.xlsx")
excel_file.close()
