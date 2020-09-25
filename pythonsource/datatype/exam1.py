#%%
# Q1) A학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는
#     다음과 같다. A 학급의 평균을 구하시오
#     70,60,55,75,95,90,80,85,100
#     [조건] 중간고사 점수를 리스트로 생성하고 평균 구하기
list1 = [70,60,55,75,95,90,80,85,100]
sum1 = 0
for i in range(0, len(list1)):
    sum1 += list1[i]
print(sum1/len(list1))

# 쌤 코딩
sum(list1)/len(list1)

#%%
# Q2) 아래 문자열의 길이를 구하시오.
#   str1 = "djwodfjoij31o5oieh52523o5oidjowjdf"
str1 = "djwodfjoij31o5oieh52523o5oidjowjdf"
print(len(str1))

#%%
# Q3) 화면에 * 기호 100개를 표시하기
for i in range(101):
    print("*", end="")

# 쌤 코딩
print("*" * 100)
#%%
# Q4) 문자열 30을 각각 정수형, 실수형, 문자형으로 변경해서 출력하기
num1 = 30
print(int(num1))       # 정수형
print(float(num1))     # 실수형
print(str(num1))       # 문자형

# 쌤 코딩 (결과값 동일)
str1 = "30"
print("정수형 :", int(str1), type(int(str1)))
print("실수형 :", float(str1), type(float(str1)))
print("문자형 :", str(str1), type(str(str1)))
#%%
# Q5) 문자열 Niceman 에서 man 문자열만 출력하기
str1 = "Niceman"
print(str1[-3:])

# 쌤 코딩
print(str1[4:])
#%%
# Q6) 문자열 http://www.daum.net 에서 http:// 제거하고 출력하기
str1 = "http://www.daum.net"
print(str1.replace("http://",""))

# 쌤 코딩
print(str1[7:])
#%%
# Q7) 문자열 abcdefghijklmn 에서 슬라이싱을 이용해 "cde"만 출력하기
str1 = "abcdefghijklmn"
print(str1[2:5])

#%%
# Q8) 다음 리스트에서 "Apple" 항목만 삭제하고 출력하기
#     ["Banana", "Apple", "Orange", "Grape"]
list1 = ["Banana", "Apple", "Orange", "Grape"]
print(list1)
del list1[1]
print(list1)

# 쌤 코딩
list2 = ["Banana", "Apple", "Orange", "Grape"]
print(list2)
list2.remove("Apple")
print(list2)
#%%
# Q9) 다음 리스트에서 '정' 글자만 제외하고 출력하기
#     ["갑","을","병","정","경"]
list1 = ["갑","을","병","정","경"]
print(list1)
del list1[3]
print(list1)

# 쌤 코딩
list2 = ["갑","을","병","정","경"]
for str in list2:
    if str != "정":
        print(str, end="")

# 컴프리헨션 적용
print("\n-- comprehension --")
list2_1 = [str for str in list2 if str != "정"]
print(list2_1)

#%%
# Q10) 다음 리스트에서 5글자 이상의 단어만 출력하기
#      ["nice", "study", "python", "anaconda", "!"]
list1 = ["nice", "study", "python", "anaconda", "!"]
for i in range(0,len(list1)):
    if len(list1[i]) >= 5:
        print(list1[i])

# 쌤 코딩
list3 = ["nice", "study", "python", "anaconda", "!"]
for str in list3:
    if len(str) >= 5:
        print(str, end=" ")

# 컴프리헨션 적용
print("\n-- comprehension --")
list1_1 = [str for str in list1 if len(str)>=5]
print(list1_1)

#%%
# Q11) 아래 리스트에서 소문자만 출력하기
#      ["A","b","c","D","e","F","G","h"]
list1 = ["A","b","c","D","e","F","G","h"]
n = len(list1)
for i in range(0,len(list1)):
    if list1[i].islower():
        print(list1[i], end=" ")

# 쌤 코딩
list4 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for str in list4:
    if str.islower():
        print(str)

# 컴프리헨션 적용
print("\n-- comprehension --")
list4_1 = [str for str in list4 if str.islower()]
print(list4_1)

#%%
# Q12) 아래 리스트에서 소문자는 대문자로 대문자는 소문자로 출력하기
#      ["A","b","c","D","e","F","G","h"]
list1 = ["A","b","c","D","e","F","G","h"]
for i in range(0,len(list1)):
    if list1[i].islower():
        print(list1[i].upper(), end=" ")
    else:
        print(list1[i].lower(), end=" ")

print()
# 쌤 코딩
list5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for ch in list5:
    if ch.islower():
        print(ch.upper(), end=" ")
    else:
        print(ch.lower(), end=" ")
print()
for ch in list5:
    print(ch.swapcase(), end=" ")

#%%
# Q13) 주차장 프로그램 작성하기
# ord : 문자를 아스키코드값으로 변환해주는 함수
# chr : 숫자를 아스키코드에 따라 문자로 변환해주는 함수
print(ord("A"))    # 65
print(ord("a"))    # 97
print(chr(65))     # A

# num = input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 : ")
# gar = []
# if num == 1:
#     for i range("A","E"):
#         gar.append(i)
#         print(i+" 자동차 들어감. 주차장 상태 ==> "+gar)

# 쌤 코딩
parking_lot = []
top, car_name = 0, "A"

while True:
    no = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 : "))

    if no <= 3:
        if no == 1:
            if top >= 5:
                print("주차장 꽉 찼음")
            else:
                parking_lot.append(car_name)
                print("%c 자동차 들어감. 주차장 상태 ==> %s" % (car_name, parking_lot))
                top += 1
                car_name = chr(ord(car_name) +1)
        if no == 2:
            if top > 0:
                outCar = parking_lot.pop()
                print("%c 자동차 들어감. 주차장 상태 ==> %s" % (car_name, parking_lot))
                top -= 1
                car_name = chr(ord(car_name) + 1)
            else:
                print("빠져나갈 자동차가 없음")
        else:
            print("프로그램 종료")
            break
    else: 
        print("번호를 확인해주세요")
