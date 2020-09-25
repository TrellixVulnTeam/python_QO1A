class UserInfo:
    """
    UserInfo class
    Author : Park
    Date : 2020.08.13
    Description : Class 작성법 / 생성자
    """
    # 생성자 : 생성자 오버로딩 개념 없음
    def __init__(self):
        self.name = "하성운"
        self.age = 27

    # Instance Method : self를 인자로 가지고 있어야 함
    def user_info(self):
        print("메소드 실행")

    def __str__(self):
        return "name : {}, age : {}".format(self.name, self.age)      

# 객체 생성
user1 = UserInfo()

# 메소드 호출
user1.user_info()

# user1 출력
print(user1)
