# Tuple
# 값을 수정할 수 없음, 읽기만 가능, 속도가 빠름

#%%
# 튜플 생성
t1 = ()
t2 = (1, 2, 3)
t3 = (1,)       # tuple은 요소가 하나라면 반드시 , 필요
t4 = 1, 2, 3
t5 = (1, 2, "Life", "is")
t6 = (1, 2, ("Life", "is"))

#%%
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)

#%%
# 튜플은 삽입, 삭제, 수정 불가 => 사용자 조작 실수로 인한 데이터 손실 방지 가능
# del t2[0]   # 삭제 불가능으로 error
# t1[0] = 1

#%%
# 인덱싱, 슬라이싱, +, *
print(t5[3])
print(t4[0:3])
print(t2[0] + t2[1])
print(t2 + t3)
print(t2 * 2)

#%%
# 튜플을 리스트로 변경 / 리스트를 튜플로 변경
print(list(t2))

list = [5, 2, 3, 4]
print(tuple(list))

#%%
# 튜플 자체 삭제
del(t2)