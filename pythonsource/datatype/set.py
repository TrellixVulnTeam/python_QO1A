# set : 중복을 혀용하지 않음 / 순서가 없음

#%%
# set 생성
set1 = set()
set2 = set([1,2,3,4])
set3 = set([1,4,5,6,6,7])

print("set1 :", set1)
print("set2 :", set2)
print("set3 :", set3)

#%%
# list, 문자열, tuple, dict로부터 set 생성
print("list -> set : ", set([1,2,3,4,65]))
print("string -> set : ", set("abcdefg"))
print("tuple -> set : ", set((1,2,3,4,65)))
print("dict -> set : ", set({"no":1,"name":"seng","age":27})) # key값만 담김

#%%
# set -> tuple, list, str
print("set -> tuple : ", tuple(set2), type(tuple(set2)))
print("set -> list : ", list(set3), type(list(set3)))
print("set -> str : ", str(set3), type(str(set3)))

#%%
# 교집합, 합집합, 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print("교집합 : ", s1.intersection(s2))
print("교집합 : ", (s1 & s2))
print()
print("합집합 : ", s1.union(s2))
print("합집합 : ", (s1 | s2))
print()
print("차집합 : ", s1.difference(s2))
print("차집합 : ", (s1 - s2))
print()
print("대칭 차집합 : ", s1.symmetric_difference(s2))
print("대칭 차집합 : ", (s1 ^ s2))

#%%
# set 요소 추가
s3 = set([7, 8, 9, 10, 15])
s3.add(18)
s3.add(7)
print(s3)

#%%
# update() : 여러개 요소 추가
s3.update([4, 5, 6])
print(s3)

#%%
# remove() : 요소 삭제
s3.remove(15)
print(s3)

#%%
# 당첨자 뽑기
from random import *

users = list(range(1, 21))
print(users)
shuffle(users)  # 섞기
print(users)

print("--- 당첨자 발표 ---")
winners = sample(users, 4)
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
