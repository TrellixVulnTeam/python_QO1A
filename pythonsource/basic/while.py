#%%
i = 1
while i < 11:
    print(i)
    i = i + 1

print()
i = 1
while i <= 10:
    print(i, end=" ")
    i = i + 1

#%%
# 1~100까지 짝수만 출력
i = 0
while i <= 100:
    i = i + 2
    print(i, end=" ")

#%%
# 1~100까지 합계를 구한 뒤 출력
i = 0
sum1 = 0     # sum이 함수로 정의되어있기 때문에 동명의 변수 선언하지않는게 좋음
while i <= 100:
    sum1 += i
    i += 1
print("1에서 100까지의 합 : {}".format(sum1))

#%%
# 3단 구구단 출력
print("3단 출력")
i = 1
while i < 10:
    print("%d * %d = %d" % (3, i, (3*i)))
    i += 1

#%%
# 사용자로부터 입력받아서 화면에 출력
# 종료는 q를 입력하면 종료
data = ""
while data != 'q':
    data = input("q를 입력하면 중단됩니다. 문자을 입력해주세요")
    print(data)
    if data == "q":
        print("종료합니다.")
