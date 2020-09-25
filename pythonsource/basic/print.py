# print함수
print("Hello Python!")        # 문자열
print(type('Hello Python!'))  # ' ' : 문자열 <class 'str'>
print(type(100))              # 정수 <class 'int'>
print("100")                  # 문자열
print(type(25.3))             # 실수 <class 'float'>
print()                       # ENTER
print(True)                   # Bool type = True, False (첫번째 글자는 대문자!)
print("""안녕하세요""")        # '''안녕하세요'''
print('T','E','S','T')        # T E S T (문자열 연달아 출력 ',' & 알아서 띄어쓰기)
print()  


# print() 옵션
# sep : 각 문자열의 구분을 무엇으로 할 것인가 지정
print('T','E','S','T', sep='')          # TEST
print('T','E','S','T', sep=',')         # T,E,S,T
print('2020','07','31', sep='-')        # 2020-07-31
print("jjae123","google.com",sep="@")   # jjae123@google.com
print()

# end : 해당 옵션이 없는 경우 print() 무조건 한 줄 출력
#       옵션을 줘서 공백을 표시 해주면 다음 라인과 연결
print("Welcome To", end=' ')
print("Python World")


