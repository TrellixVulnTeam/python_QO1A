#%% 1번
print("*" * 30)
print("1부터 n까지 정수의 합 구하기")
print("*" * 30)
num = int(input("합을 구하고 싶은 정수를 입력하세요"))
print("1 ~ ", num, "의 합 : {}".format(sum(range(1, num))))

#%% 2번
menu = input("어떤 커피 드릴까요? (1:보통, 2:설탕, 3:블랙)")

def coffee_machine(menu):
    if menu == "1":
        sel3 = "# 3. (자동으로) 보통 커피를 탄다"
    elif menu == "2":
        sel3 = "# 3. (자동으로) 설탕 커피를 탄다"
    elif menu == "3":
        sel3 = "# 3. (자동으로) 블랙 커피를 탄다"
    else:
        sel3 = "# 3. (자동으로) 아무거나 탄다"

    print("# 1. (자동으로) 뜨거운 물을 준비한다.")
    print("# 2. (자동으로) 종이컵을 준비한다.")
    print(sel3)
    print("# 4. (자동으로) 물을 붓는다.")
    print("# 5. (자동으로) 스푼으로 저어서 녹인다.")
    print()
    print("손님 커피 여기 있습니다.")

coffee_machine(menu)

#%% 3번 문제 풀이
for i in range(5):
    for j in range(5):
        if i <= j:
            print("*", end=" ")
    print()

#%% 4번
class Person:
    name = ""
    age = 0

    def __inif__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

person = Person("홍길동", 25)
print("이름 : ", person.get_name())
print("나이 : ", person.get_age())

#%% 5번

pip install pymysql
