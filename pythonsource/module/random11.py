import random

# random() : 0.0 <= x < 1.0 사이의 값 리턴
print(random.random())
# randrange(max) : 0~max 사이의 값 리턴
# randrange(min,max) : min~max 사이의 값 리턴
print(random.randrange(10))
# uniform(min,max) : 지정한 범위 사이의 float 리턴
print(random.uniform(10, 20))
# choice(list) : 리스트 내부의 요소를 랜덤하게 선택
print(random.choice([1, 2, 3, 4, 5, 6, 7]))
# shuffle(list) : 리스트 내부의 요소를 랜덤하게 섞기
print(random.shuffle([1, 2, 3, 4, 5, 6, 7]))
# sample(list, k=숫자) : 리스트의 요소 중에서 k 개 뽑기
print(random.sample([1, 2, 3, 4, 5, 6, 7], k=2))
