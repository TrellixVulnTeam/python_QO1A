# 변수 : 정수형, 문자형, 실수형, 불린형
#        타입을 지정하지 않음(값을 할당 받으면 타입이 결정됨)

str1 = "Life is too short, You need Python"
str2 = "123"

num1 = 10
num2 = 10.5

num3 = num4 = 20     # 변수 2개 한번에 같은 값으로 선언 가능
print("num3 = ",num4)
print("num3 = ",num3)
print()

num5, num6 = 10, 20  # 다른 값을 연달아 변수 선언 가능
print("num5 = %d, num6 = %d" % (num5, num6))
print()

# num5와 num6의 값을 서로 바꿔서 출력
num5, num6 = num6, num5
print("num5 = %d, num6 = %d" % (num5, num6))
print()

str3 = 500
print(str3, type(str3))  # 500 <class 'int'>
str3 = "Hello"
print(str3, type(str3))  # Hello <class 'str'>
print()

# 정수형 값
a = 123
b = -178
c = 0

# 실수형 값
a = 1.2
b = -3.45
c = 4.24e10         # e : 지수
d = 4.24e-10
print("c : ", c)
print("d : ", d)
print()

# 8진수, 16진수
print(0o177)     # 0o : 8진수로 계산 (1*7 + 8*7 + 8*8*1)
print(0x1511)   # 0x : 16진수로 계산 (1*1 + 16*1 + 16*16*5 + 16*16*16*1)

# type() : 변수의 타입을 확인
# 변수의 타입을 변경 : str() - 문자열로 변경
print("\n---변수 타입 확인 및 변경---")
a = 3
print("a 타입 : ", type(a))          # a 타입 : <class 'int'>
print("a 타입 : ", type(str(a)))     # a 타입 : <class 'str'>
print("1.2 타입 : ", type(str(1.2))) # 1.2 타입 :  <class 'str'>
print("True 타입 : ", type(str(True)), str(True))
print()

# 변수의 타입을 변경 : int() - 정수형으로 변경 (반올림안하고 절삭)
print("True 타입 : ", type(int(True)), int(True))  # print(int(False)) = 0
print("1.2 타입 : ", type(str(1.2)), int(1.2))
print("3.5 타입 : ", type(str(3.5)), int(3.5))
print("'99' 타입 : ", type(int("99")), int("99"))
# 소수점, 지수를 포함하는 문자열은 정수형으로 변경
# print("'99.5' 타입 : ", type(int("99.5")), int("99.5")) 예외 발생
print()

# 변수의 타입을 변경 : float() - 실수형으로 변경
print("True 타입 : ", type(float(True)), float(True))
print("False 타입 : ", type(float(False)), float(False))
print("'99.5' 타입 : ", type(float("99.5")), float("99.5"))
print("'99' 타입 : ", type(float("99")), float("99"))
print()

# 변수의 타입을 변경 : bool() - boolean형으로 변경
print("'99' 타입 : ", type(bool(99)), bool(99))
print("0 타입 : ", type(bool("0")), bool("0"))
print("99 타입 : ", type(bool("99")), bool("99"))
print("0.1 타입 : ", type(bool(0.1)), bool(0.1))
print("0 타입 : ", type(bool(0)), bool(0))
print("1 타입 : ", type(bool(1)), bool(1))

