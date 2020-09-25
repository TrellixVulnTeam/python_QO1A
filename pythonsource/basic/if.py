#%%
# if 조건문 :
#   실행할 문장 (★띄어쓰기는 4칸★)

if True:
    print("True")

#%%
a = 200
if a < 100:
    print("a는 100보다 작다")
print("조건문에서 들여쓰기는 중요함")

#%%
a = 300
# if a > 200 and a <= 300:
if 200 < a <= 300:
    print("a는 200과 300 사이에 있다")

#%%
a, b, c = 12, 6, 18

# 가장 큰 값 출력
max = a
if max < b:
    max = b
if max < c:
    max = c

print('제일 큰 수 : ', max)

#%%
# if 조건문:
#   수행문장
# else:
#   수행문장

if True:
    print("True")
else:
    print("False")

#%%
a = 55
if a < 100:
    print('a는 100보다 작다')
else:
    print("a는 100보다 크다")

#%%
score, grade = 90, "A"
if score >= 90 and grade == "A":
    print("합격")
else:
    print("불합격")

#%%
# 사용자에게 숫자를 입력받아 그 숫자가 짝수, 홀수인지
# 판별하기
num = int(input("숫자를 입력해주세요 :"))

if num % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

#%%
import datetime

now = datetime.datetime.now()  # datetime module 안에 datetime class 안에 now함수 호출

print(now)
print(
    "{}년 {}월 {}일 {}시 {}분 {}초".format(
        now.year, now.month, now.day, now.hour,
        now.minute, now.second
    )
)

# 오전/오후인지 출력하기
if now.hour <=12:
    print("오전입니다")
else:
    print("오후입니다")

#%%
a = 86
if a > 50:
    if a < 100:
        print("50보다 크고 100보다 작다")
    else:
        print("와~~ 100보다 크군요")
else:
    print("50보다 작다")

#%%
score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")

#%%
# 다중조건 : if ~ elif ~ else
num1 = 90
if num1 >= 90:
    print("A")
elif num1 >= 80:
    print("B")
elif num1 >= 70:
    print("C")
else:
    print("D")

#%%
# 계절확인 -> 봄/여름/가을/겨울 중에서 하나 출력하기
# 3~5 : 봄 / 6~8 : 여름 / 9~11 : 가을 / 12~2 : 겨울

import datetime

month = datetime.datetime.now().month

if 3 <= month <= 5:
    print("봄")
elif 6 <= month <=8:
    print("여름")
elif 9 <= month <=11:
    print("가을")
else:
    print("겨울")

#%%
# 계산기 프로그램
# 두 개의 숫자와 연산자를 입력받아 계산한 후 출력하는 프로그램
# +, -, *, /, //, %, **

num1 = int(input("첫번째 숫자를 입력하세요 : "))
op = input("+,-,*,/,//,%,** 중 연산자 입력 ")
num2 = int(input("두번째 숫자를 입력하세요 : "))
result = 0
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
elif op == "//":
    result = num1 // num2
elif op == "%":
    result = num1 % num2
else:
    result = num1 ** num2

print("%d %s %d = %d" % (num1, op, num2, result))

#%%
# pass
if True:
    pass    # 나중에 구현할 부분
else:
    pass
