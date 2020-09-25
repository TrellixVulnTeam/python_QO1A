# 산술 연산자 : +, -, *, /, %, //, **
a = 3
b = 4
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)    # 소수점까지 출력
print("a // b = ", a // b)  # 정수 나누기 연산자(java에서 나누기 연산자와 결과값 동일)
print("a ** b = ", a ** b)  # 지수 제곱 연산자
print()

a, b, c = 2, 3, 4
print(a + b - c, a + b * c, a + b / c)
print()

s1, s2, s3 = "100", "100.123", "99999999"
print(s1 + s2 + s3)  # 문자열과 + : 연결
print(float(s1) + float(s2) + float(s3))
# print(s1 + 1)  # 에러발생
print(int(s1) + 1)
print()


# 동전 교환하기
money = 7777
# 500원 : 00개, 100원 : 0개, 50원 : 0개, 10원 : 0개, 나머지돈 : 원
c500 = money // 500
money = money % 500
c100 = money // 100
money = money % 100
c50 = money // 50
money = money % 50
c10 = money // 10
money = money % 10
print("{} : {}개, {} : {}개, {} : {}개, {} : {}개, 나머지돈 : {}원".format("500원", c500, "100원", c100, "50원", c50, "10원", c10, money))


#%%
# 대입 연산자
a = 10
a += 5    # a = a + 5
print(a)
a -= 5    # a = a - 5
print(a)
a *= 5    # a = a * 5
print(a)
a /= 5    # a = a / 5    (나누었을 때 실수까지)
print(a)
a //= 5   # a = a // 5   (나누었을 때 정수까지만)
print(a)
a %= 5    # a = a % 5
print(a)
a **= 5   # a = a ** 5   (제곱)
print(a)

#%%
# 관계 연산자 : ==, !=, >, >=, <, <=
a, b = 10, 0
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

#%%
# 논리연산자 : and, or, not
a, b, c = 100, 60, 15
print("and : ", a > b and b > c)
print("or : ", a > b or b < c)
print("not : ", not b < c)

#%%
# 비트 연산자 : &(하나만 1이면 0), |(하나만 1이어도 1)
a, b, c = 100, 60, 15
print("& : ", 10 & 7)   # 1010 & 0111 = 0010
print("| : ", 10 | 7)   # 1010 | 0111 = 1111
print("& : ", (a > b) & (b < c))  # 0001 & 0000 = 0000
print("| : ", (a > b) | (b < c))  # 0001 | 0000 = 0001
