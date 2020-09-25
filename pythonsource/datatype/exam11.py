#%%
# q1) A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는
#     다음과 같다. A 학급의 평균을 구하시오
#     70,60,55,75,95,90,80,85,100
#     [조건] 중간고사 점수를 리스트로 생성하고 평균 구하기
a_class = [70, 60, 55, 75, 95, 90, 80, 85, 100]
total = 0
for num in a_class:
    total += num
print("A 학급 평균 : %.2f" % (total / len(a_class)))
print()
print("A 학급 평균 : %.2f" % (sum(a_class) / len(a_class)))
#%%
# q2) 아래 문자열의 길이를 구하시오.
str1 = "dk2jd23iljdk2jd93fdkedieliddkfiejfied"
print(len(str1))

#%%
# q3) 화면에 * 기호 100개를 표시하기
print("*" * 100)

#%%
# q4) 문자열 30을 각각 정수형, 실수형, 문자형으로 변경해서 출력하기
str1 = "30"
print("정수형 :", int(str1), type(int(str1)))
print("실수형 :", float(str1), type(float(str1)))
print("문자형 :", str(str1), type(str(str1)))


#%%
# q5) 문자열 Niceman 에서 man 문자열만 출력하기
str1 = "Niceman"
print(str1[4:])

#%%
# q6) 문자열 http://www.daum.net 에서 http:// 제거하고 출력하기

url = "http://www.daum.net"
print(url[7:])

print(url.replace("http://", ""))

#%%
# q7) 문자열 abcdefghijklmn 에서 슬라이싱을 이용해 "cde" 만 출력하기

str1 = "abcdefghijklmn"
print(str1[2:5])

#%%
# q8) 다음 리스트에서 "Apple" 항목만 삭제하고 출력하기
#     ["Banana","Apple","Orange","Grape"]
list1 = ["Banana", "Apple", "Orange", "Grape"]
list1.remove("Apple")  # del list1[1]
print(list1)


#%%
# q9) 다음 리스트에서 '정' 글자만 제외하고 출력하기
list2 = ["갑", "을", "병", "정", "경"]
for str in list2:
    if str != "정":
        print(str, end="")

#%%
# q10) 다음 리스트에서 5글자 이상의 단어만 출력하기
list3 = ["nice", "study", "python", "anaconda", "!"]
for str in list3:
    if len(str) >= 5:
        print(str, end=" ")

#%%
# q11) 아래 리스트에서 소문자만 출력하기
list4 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for str in list4:
    if str.islower():
        print(str)

#%%
# q12) 아래 리스트에서 소문자는 대문자로 대문자는 소문자로 출력하기
list5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for ch in list5:
    if ch.islower():
        print(ch.upper(), end=" ")
    else:
        print(ch.lower(), end=" ")

#%%
#  q13) 주차장 프로그램 작성하기
#

