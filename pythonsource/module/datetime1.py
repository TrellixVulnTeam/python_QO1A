# date(날짜) / time(시간) 과 관련된 모듈
import datetime

# 현재 시각 구하기
now = datetime.datetime.now()
print(now)
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()
print(now.strftime("%Y.%m.%d %H:%M:%S"))
