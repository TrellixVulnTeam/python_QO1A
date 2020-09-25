class SelfTest:
    # 클래스 메소드
    @classmethod
    def fuction1(cls):
        print("function1() called")
    
    def fuction2(self):   # self를 넣음으로써 인스턴스 메소드가 됨
        print("function2() called")

self_test = SelfTest()
# 클래스 메소드 호출하는 방법
self_test.fuction1()
SelfTest.fuction1()  # 클래스명.클래스메소드() 로 접근하는게 더 명확함

# 인스턴스 메소드 호출하는 방법
self_test.fuction2()
SelfTest.fuction2(self_test)