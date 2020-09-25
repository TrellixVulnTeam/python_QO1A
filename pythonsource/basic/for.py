# for

#%%
# range() : 범위 지정
# range(시작값, 마지막값, 증가값)

print(range(5))          # 0~5
print(list(range(5)))    # [0, 1, 2, 3, 4]
print(list(range(1,5)))  # [1, 2, 3, 4]
print(list(range(0,10,2)))  # [0, 2, 4, 6, 8]

#%%
# 0~9까지 출력
for i in range(10):
    print(i)

#%%
# 1~10까지 출력
for i in range(1,11):
    print(i)

#%%
# 1~100까지 출력
# 1 2 3 4 ~~
for i in range(1,101):
    print(i, end=" ")

#%%
# 1~10 사이에 짝수만 출력
for i in range(2,11,2):
    print(i, end=" ")
    
#%%
# 1~100까지 합계를 구한 후 출력
sum0 = 0
for i in range(1,101):
    sum0 += i
print("1~100까지 합 : ", sum0)    

#%%
# 사용자로부터 숫자를 입력받아
# 1~ 사용자가 입력한 숫자까지 합계를 구한 뒤 출력
num = int(input("숫자 입력"))
sum1 = 0
for i in range(1, num+1):
    sum1 += i
print("1 ~ %d 합 : %d" % (num, sum1))

#%%
for i in range(4, -1, -1):
    print(i, end=" ")

#%%
# 합계 구할 때 for문 필요없이 sum함수 사용 가능
print(sum(range(1, 101)))   # 1~100까지의 합
print(sum(range(1, 101, 2)))   # 1~100까지 홀수 합

#%%
# for [] in [하나씩 꺼내 쓸 수 있는 형태]
word = "dreams"
for s in word:
    print(s)

#%%
# 3단 출력
result = 0
for i in range(1, 10):
    result = 3 * i
    print("%d * %d = %d" % (3, i, result))

#%%
# 이중 for문
for i in range(3):
    for j in range(3):
        print(j, end = " ")
    print()

#%%
# 3 * 3 찍기
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

#%%
# 0 1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
# 4 5 6 7 8
# 내 코딩
for i in range(0,5):
    for j in range(i,i+5):
        print(j, end = " ")
    print()

print()
# 쌤 코딩
for i in range(5):
    for j in range(5):
        print(i + j, end = " ")
    print()

#%%
# 2~9단 출력
# 2 * 1 = 2  2 * 2 = 4 ~~
# 3 * 1 = 3
for i in range(2,10):
    for j in range(1,10):
        print("%d * %d = %d" % (i , j ,i * j), end = "  ")
    print()

#%%
# 2~9단 출력
# 2 * 1 = 2  3 * 1 = 3 ~~
# 2 * 2 = 4
for i in range(1,10):
    for j in range(2,10):
        print("%d * %d = %d" % (j , i ,i * j), end = "\t")
    print()

#%%
# break
i = 1
while i <= 10:
    if i == 5:
        break
    print(i, end=" ")
    i += 1

#%%
# continue
i = 1
while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    print(i, end=" ")

#%%
# if문에서 continue
# 1~10까지 출력하기 (단, 5 제외)
for i in range(11):
    if i == 5:
        continue
    print(i, end=" ")

#%%
# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(5):
    for j in range(5):
        if j <= i:
            print("＊", end=" ")
    print()
