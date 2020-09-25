import requests
import openpyxl
import pprint

# 네이버 open api 에서 도서 정보 검색 후 엑셀로 저장
# 도서정보 - isbn, title, price, discount
# 엑셀 필드명 - 번호, isbn, 도서명, 가격, 할인가격

# 엑셀 저장
excel_file = openpyxl.Workbook()
# 기본으로 만들어진 시트 활성화
sheet1 = excel_file.active
# 시트의 열 너비 조절
sheet1.column_dimensions['B'].width = 30    # isbn
sheet1.column_dimensions['C'].width = 100   # title
sheet1.column_dimensions['D'].width = 15    # price
sheet1.column_dimensions['E'].width = 15    # discount
# 타이틀 행 삽입
sheet1.append(["번호", "isbn", "도서명", "가격", "할인가격"])
# 시트 이름 변경
sheet1.title = "도서목록"

# 네이버 오픈API를 이용한 도서 정보 가져오기
url = "https://openapi.naver.com/v1/search/book.json"

start, num = 1, 0

for idx in range(3):
    # 1, 101, 201
    start_num = start + (idx * 100)

    param = {
        "query" : "YBM",
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
            product_info = [num, item['isbn'], item['title'], item['price'], item['discount']]
            sheet1.append(product_info)
    else:
        print("Error", res.status_code)

excel_file.save("./resources/도서목록.xlsx")
excel_file.close()
