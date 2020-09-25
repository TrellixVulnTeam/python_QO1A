from sum1 import sum

print(sum(50, 55))  # 위에 import 구문 때문에 print(sum1.sum(50, 55)) 에서 sum1 빼야함
# sum1 모듈 안에서 sum 함수만 사용하겠다고 선언했기 때문에
# 아래 구문 실행 불가
# print(sum1.safe_sum(50, "55"))
# print(sum1.safe_sum(50, 60))
