# 예외상황
# 컴파일 예외 => 문법적인 에러
# 런타임 예외 => 실행 후에 나타나는 에러 (개발자의 능력)

#%%
# print("Test)

#%%
a, b = 10, 15
# print(c) # NameError : 참조 변수 없음

#%%
# 런타임 예외
# print(10 / 0) # ZeroDivisionError: division by zero

#%%
list = [10, 20, 30]
# print(list[0])
# print(list[3]) # IndexError: list index out of range

#%%
dict = {"name":"Ha","age":27, "city":"seoul"}
# print(dict["hobby"]) # KeyError: 'hobby'
# print(dict.get("hobby")) # None --> error를 방지

#%%
x = [1, 5, 9]
# x.remove(10) # ValueError: list.remove(x): x not in list
x.index(10) # ValueError: 10 is not in list

#%%
# ValueError
number_input = int(input("정수입력 >> "))
print("원 반지름 :", number_input)
print("원 둘레 :", 2 * 3.14 * number_input)
print("원 넓이 :", 3.14 * number_input * number_input)

#%%
# TypeError
x = [1, 2] # list
y = (3, 4) # tuple
# print(x + y)
print(x + list(y))
