# 메소드 오버라이딩
class Parent:
    def func1(self):
        print("Parent func1()")

    def func2(self):
        print("Parent func2()")


class Child(Parent):
    def func1(self):
        print("Child func1()")

    def func3(self):
        print("Child func3()")

parent, child = Parent(), Child()

parent.func1()
parent.func2()
child.func1()
child.func2()
child.func3()
