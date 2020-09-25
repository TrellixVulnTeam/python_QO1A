# 클래스 상속
# class [자식클래스명]([부모클래스명]):
class Parent:       # 부모클래스
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 호출")

    def test(self):
        print("Parent 클래스의 test() 호출")

class Child(Parent):        # 자식클래스
    def __init__(self):
        Parent.__init__(self)       # 부모생성자 호출방법1. [부모클래스명].부모생성자명(self)  // self 꼭!
        print("Child 클래스의 __init()__ 호출")

child = Child()
child.test()
print(child.value)
