import re
import openpyxl

# " VS "로 문자열 분리하기
string = "python VS java"
pattern = re.compile(r" VS ")
print(pattern.split(string))

# 주민번호의 - 기호를 * 로 바꿔서 출력하기
string = "801210-1011323"
pattern = re.compile(r"-")
print(pattern.sub("*", string))
print(re.sub(pattern, "*", string))

# data_kr.xlsx를 읽어서 주민번호 뒷자리를 *로 바꿔서 출력하기
excel_file = openpyxl.load_workbook("./resources/data_kr.xlsx")
sheet1 = excel_file.active

pattern = re.compile(r"[0-9]{7}")

for item in sheet1.rows:
    print(re.sub(pattern, "*******", item[1].value))


excel_file.close()
