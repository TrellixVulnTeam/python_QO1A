# %d : 정수, %f : 실수, %s : 문자열, %c : 문자
print("%d" % 100)       # 정수 100 출력
print("%5d" % 100)      # 5자리에서 오른쪽 정렬로
print("%05d" % 100)     # 비워둔 자리에 0을 채워줘
print()
print("%5s" % "hi")     # 5자리에서 오른쪽 정렬로
print("%s" % "hi")      # 문자열 hi 출력
print()
print("%-8.2f" % 123.21)
print("%8.2f" % 123.21)
print("%8.5f" % 123.2134567)    # 8자리 중 소수점 5째 자리수까지 보여줘
print()

print("I eat %d apples" % 3)
print("I eat %s apples" % "five")
number = 4                          # type 지정 없이 변수 선언 가능
print("I eat %d apples" % number)
print("I eat", number, "apples")
print()

# 문자를 2개 넣는 경우
print("%d : %s" % (1, "하성운"))    # 여러 종류의 문자를 넣을 때는 ()가 필요함!
# 2 : 김성호 - 93.25 출력해보기
print("%d : %s - %.2f" % (2, "김성호", 93.25))
print("Test 1 : %c" % "t")
# 비율 : 98% 출력
print("비율 : %d%%" % 98)   # %% : %가 문자임을 표시

