# 파이썬 데이터 타입
# 정수형
# 문자형 : '', "" 둘 다 허용, '''....''', """...."""

#%%
a = "Life is too short, You need Python"
a = '''\
    여러줄 표현시 사용
    Life is too short, You need Python
'''
print(a)

#%%
# 문자열 응용
# + : 결합
print("Python " + "is Fun")   # Python is Fun

# * : 복제
print("파이썬" * 2)     # 파이썬파이썬

#%%
print("*" * 50)
print("My Program")
print("*" * 50)

#%%
# 인덱싱
str1 = "Life is too short"
print(str1[3])    # e      / 0,1,2,3 [4번째]
print("str1[3]", str1[3]) # 기준 : 왼쪽
print("str1[3]", str1[-3]) # 기준 : 오른쪽

#%%
# 슬라이싱 - 중요도 높음
print("str1[0:4]", str1[0:4]) # Life
print("str1[5:7]", str1[5:7]) # is
print("str1[8:11]", str1[8:11]) # too
print("str1[0:-4]", str1[0:-4]) # Life is too s
print("str1[:]", str1[:]) # Life is too short  / 전체 문자열
print("str1[:17]", str1[:17]) # Life is too short
print("str1[4:]", str1[4:]) # is too short

#%%
str2 = "20200804Rainny"

# 20200804
date = str2[:8]
print(date)
# Rainny
weather = str2[8:]
print(weather)
# 2020-08-04
year = date[:4]
month = date[4:6]
day = date[6:]
print(year, month, day, sep="-")

#%%
# 주민등록번호에서 8번째 자리숫자를 사용해서
# 남자, 여자 판별하기
# 1,3 => 남자 / 2,4 => 여자
str1 = "901205-3234567"

g = str1[7:8]
if g == "1" or g == "3":
    print("남자입니다.")
else:
    print("여자입니다.")

#%%
# 각 문자의 끝에 $ 찍기
# 대$한$민$국
# 내 코딩
str2 = "대한민국"   
x = str2[0:1]
y = str2[1:2]
z = str2[2:3]
q = str2[3:4]
print(x,y,z,q, sep="$")
# 쌤 코딩
for s in str1:
    print(s + "$", end="")

#%%
# 입력받은 숫자만큼 하트를 출력
str3 = input("숫자를 입력하세요")
# 54321
# 문자의 길이 => 반복 횟수
# 5 => ♥ 5번 출력
for i in range(0, len(str3)):
    for s in range(0, int(str3[i])):
        print("♥", end=" ")
    print()

#%%
# 문자열 관련 함수 - 1. count : 문자열에 포함된 특정 문자열의 개수
str1 = "hobby"
print("str1에 포함된 b 문자열 개수 :", str1.count("b"))

#%%
# 문자열 관련 함수 - 2. find : 문자열 찾기
str1 = "Python is best Choice"
print("b가 시작되는 첫번째 위치 :", str1.find("b"))
print("o가 시작되는 첫번째 위치 :", str1.find("o"))
print("k가 시작되는 첫번째 위치 :", str1.find("k"))    # -1(못찾는 경우)

print("6번째 이후로 o가 시작되는 위치 :", str1.find("o",6))

#%%
# 문자열 관련 함수 - 3. index : 문자열 찾기
print("b가 시작되는 첫번째 위치 :", str1.index("b"))
print("o가 시작되는 첫번째 위치 :", str1.index("o"))
print("k가 시작되는 첫번째 위치 :", str1.index("k"))  # error

#%%
# 문자열 관련 함수 - 4. startwith / endswith : 특정 문자열로 시작 혹은 끝나는 지 확인
str1 = "Python is easy programming"
print(str1.startswith("P"))   # True
print(str1.endswith("h"))     # False

#%%
# 문자열 관련 함수 - 5. join : 문자열 연결
a = ","
print("문자열 연결", a.join("abcde"))
print("a","b","c","d","e", sep=a)
# 리스트를 일반 문자열로 변경할 때 주로 쓰임
# " ".join(리스트)

# %%
# 문자열 관련 함수 - 6. upper / lower : 대/소문자 변환
str1 = "abcde"
print("대문자로 변경 :", str1.upper())
str2 = "ABCDE"
print("소문자로 변경 :", str2.lower())

# %%
# 문자열 관련 함수 - 7. swapcase : 대/소문자 상호 변환
str1 = "Python Is Easy"
print(str1.swapcase())

# %%
# 문자열 관련 함수 - 8. title : 각 단어의 시작을 대문자로 변환
str1 = "python is easy"
print(str1.title())

# %%
# 문자열 관련 함수 - 9. strip / lstrip / rstrip : 공백 제거
str1="       hi"
print(str1.strip())
print(str1.lstrip())    # 왼쪽 공백 제거
str1="hi       "
print(str1.strip())
print(str1.rstrip())    # 오른쪽 공백 제거
str1="     hi     "
print(str1.strip())     # 양쪽 공백 제거

#%%
# 문자열 관련 함수 - 10. replace : 문자열 바꾸기
str1 = "Life is too short"
print(str1.replace("Life", "Your leg"))

#%%
# 문자열 관련 함수 - 11. split : 특정 문자로 문자열 나누기
str1 = "Life is too short"
print(str1.split())       # ['Life', 'is', 'too', 'short'] (리스트)
str2 = "Life:is:too:short"
print(str2.split(":"))    # ['Life', 'is', 'too', 'short'] (리스트)

str3 = "List\nis\ntoo\nshort"
print(str3.splitlines())  # ['Life', 'is', 'too', 'short'] (리스트)
# 리스트의 결과를 문자열로 변경
print(" ".join(str3.splitlines()))

#%%
# 문자열 관련 함수 - 12. center/ljust/rjust/zfill - 문자열 정렬
str1 = "파이썬"
print(str1.center(10, "*"))
print(str1.ljust(10, "*"))
print(str1.rjust(10, "*"))
print(str1.zfill(10))   # 빈 공간은 0으로 채우면서 오른쪽 정렬

#%%
# 문자열 관련 함수 - 13. 문자열 구성 파악
print('1234'.isdigit())    # 정수형태인지
print("abcd".isalpha())    # 알파벳으로 구성되었는지
print("abc123".isalnum())  # 알파벳과 숫자로 구성되었는지
print("abcd".islower())    # 소문자인지
print("ABCD".isupper())    # 대문자인지
print("    ".isspace())    # 공백인지

#%%
# 대문자는 소문자로, 소문자는 대문자로 변경 후 출력하기
# name = "KennRY"  (swapcase() 사용하지 말기)
name = "KennRY"
# 내 코딩
for i in range(0, len(name)):
    if name[i:i+1].isupper():
        print(name[i:i+1].lower(), end="")
    else:
        print(name[i:i+1].upper(), end="")

print()
# 쌤 코딩
for s in name:
    if s.isupper():
        print(s.lower(), end="")
    else:
        print(s.upper(), end="")

#%%
# 사용자로부터 년/월/일 형태의 데이터를 입력받고
# 10년 후의 날짜를 출력하여 보여주기
# 입력값 2020/08/05  => 2030년 08월 05일
str1 = input("년/월/일 형식의 날짜를 입력해주세요")
y = "년"
m = "월"
d = "일"

# print(list(y,m,d))

print(y,m,d.join(str1.split("/")))
# print(" ".join(str1.splitlines()))


# 쌤 코딩
date1 = input("날짜입력(년/월/일 형태) ")
pos = date1.find("/")
year = int(date1[0:pos]) + 10
print(
    "입력한 날짜의 10년 후는 %s" % (str(year) + "년" + date1[5:7] + "월" + date1[8:] + "일")
)

# 리스트 형태일때
date1 = input("날짜입력(년/월/일 형태) ")
date1 = date1.split("/")  # ['2020','08','05']
print("입력한 날짜의 10년 후는 %s" % (str(int(date1[0])+10) + "년" + date1[1] + "월" + date1[2] + "일")

#%%
# 웹 사이트 주소를 이용한 비밀번호 생성하기
# https://naver.com  => nav51!
# 규칙 1 : https:// 이 부분은 제외
# 규칙 2 : 처음 만나는 점(.) 이후의 부분은 제외 => com 제외
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수
#           + "!" 구성
url = "https://naver.com"
url = url.replace("https://","")
url = url[:url.find(".")]
e_count = url.count("e")

password = url[:3]+str(len(url))+str(e_count)+"!"
print(password)
