# 파일 읽기

#%%
f = open("../resource/test1.txt", "r", encoding="utf-8")
print(f.read())
f.close()

#%%
with open("../resource/test1.txt", "r", encoding="utf-8") as f:
    print(f.read())

#%%
# 전체 읽어오기
with open("../resource/review.txt", "r", encoding="utf-8") as f:
    print(f.read())

#%%
# 줄 단위로 읽어오기(줄마다 enter)
with open("../resource/review.txt", "r", encoding="utf-8") as f:
    for c in f:
        print(c)

#%%
# 줄 단위로 읽어오기
with open("../resource/review.txt", "r", encoding="utf-8") as f:
    for c in f:
        print(c.strip())

#%%
# readline() + for문
with open("../resource/review.txt", "r", encoding="utf-8") as f:
    # print(f.readline())
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()

#%%
# readlines() : 파일 전체 내용을 리스트 구조로 반환
with open("../resource/review.txt", "r", encoding="utf-8") as f:
    print(f.readlines())

#%%
# readlines() + for문 => list구조 해체
with open("../resource/review.txt", "r", encoding="utf-8") as f:
    content = f.readlines()
    for c in content:
        print(c, end="")

#%%
# score.txt 를 읽어와서 평균을 구한 후 화면에 출력
# with open("../resource/score.txt", "r", encoding="utf-8") as f:
#     list1 = []
#     for i in range(6):
#         list1.append(f.readline().strip())
#     print(list1)  
# print(list1)
# sum(list1)/len(list1)

print()
# 쌤 코딩
with open("../resource/score.txt", "r", encoding="utf-8") as f:
    score = []
    for num in f:
        score.append(int(num))
print("평균 :", sum(score) / len(score))
print("평균 : %.2f" % (sum(score) / len(score)))

#%%
# score.txt 를 읽어와서 총합과 평균을 구한 후
# 구한 결과값을 result.txt 쓰기
# 예시
# 총합 : 790
# 평균 : 79.00
# with open("../resource/score.txt", "r", encoding="utf-8") as f:
#     score = []
#     for num in f:
#         score.append(int(num))
# sum1 = sum(score)
# avg1 = (sum(score) / len(score))

# with open("../resource/result.txt", "w", encoding="utf-8") as f:
#     f.write("총합 : ")
#     f.write(str(sum1))
#     f.write("\n평균 : ")
#     f.write(str(avg1))

# 쌤 코딩
score = []
with open("../resource/score.txt", "r", encoding="utf-8") as f:
    for num in f:
        score.append(int(num))

with open("../resource/result.txt", "w", encoding="utf-8") as f1:
    f1.write("총합 : %d\n" % sum(score))
    f1.write("평균 : %.2f\n" % (sum(score) / len(score)))

#%%
# 특정 경로의 파일을 읽어 사용자가 지정하는 폴더로 복사
import os   # 운영체제와 관련된 기능을 가진 모듈(폴더생성, 폴더목록보기) / Python제공 기본 모듈 (java.lang.과 동일)
content = ""
# 사용자에게 읽을 파일을 입력받고 저장할 폴더와 이름도 입력받기
# fName = ""
 
# 파일이 존재하면 읽은 후 사용자가 입력한 저장 폴더에 읽은
# 파일을 저장하기
# os.path.exists("D:/temp/test.txt")

# 내 코딩 안댐
# fName = input("복사할 파일의 경로와 이름을 입력해주세요")
# content = input("저장할 폴더와 이름을 입력해주세요")

# with open(fName, "r", encoding="utf-8") as f:
#     if os.path.exists(fName):
#         with open(content, "w", encoding="utf-8") as f1:
#             f1.write(f.read())
#     else:
#         print("해당 파일이 존재하지 않습니다.")

# 쌤 코딩
fName = input("복사할 파일의 경로와 이름을 입력해주세요")
if os.path.exists(fName):
    with open(fName, "r", encoding="utf-8") as inFp:
        content = inFp.read()

    oName = input("저장할 폴더와 이름을 입력하세요")
    with open(oName, "w", encoding="utf-8") as outFp:
        outFp.writelines(content)
else:
    print("%s 파일이 존재하지 않습니다." % fName)

#%%
# info.txt 파일을 읽어 BMI 지수를 계산한 후 화면에 출력하기
# bmi 지수 계산 = 체중 / (키/100)**2
# bmi 지수가 25 이상이면 과체중
#           18.5 이상이면 정상 체중
#                미만이면 저체중

# 출력 결과
# 이름 : 가나
# 몸무게 : 45
# 키 : 150
# BMI : 12.125645
# 결과 : 저체중

# with open("../resource/info.txt", "r", encoding="utf-8") as f:
#     content = f.readline()
#     name = content[0:2]
#     h = int(content[4:7])
#     w = int(content[9:11])
#     bmi = w / (h/100)**2
#     result = ""
#     if bmi >= 25:
#         result = "과체중"
#     elif 18.5 <= bmi < 25:
#         result = "정상체중"
#     elif bmi < 18.5:
#         result = "저체중"
    
#     with open("../resource/result.txt", "w", encoding="utf-8") as f1:
#         f1.write("이름 :",name)
#         f1.write("몸무게 :",)

# 쌤 코딩
with open("../resource/info.txt", "r", encoding="utf-8") as f:
    for info in f:
        name, height, weight = info.strip().split(", ")
        # print(name, height, weight)
        result = ""
        bmi = int(weight) / ((int(height)/100)**2)
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상체중"
        else:
            result = "저체중"
        print(
            "\n".join(["이름 : {}", "몸무게 : {}", "키 : {}", "BMI : {}", "결과 : {}"]
            ).format(name, weight, height, bmi, result)
        )
        print()

#%%
# 이진파일
# rb : readbinary / wb : writebinary

data = ""
try:
    with open("c:/windows/notepad.exe", "rb") as f1:
        data = f1.read()
    
    with open("c:/temp/notepad.exe", "wb") as f2:
        f2.write(data)
except:
    print("복사 실패")
