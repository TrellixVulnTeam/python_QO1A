class Student():  # ()는 필수요소가 아님
    def __init__(self, name, number, grade, details):   # self 반드시 존재(인스턴스 메소드) / java의 this.과 동일
        self.name = name      # 인스턴스 변수
        self.number = number
        self.grade = grade
        self.details = details
    
    def __str__(self):      # java의 toString() 기능
        return "{},{},{},{}".format(self.name, self.number, self.grade, self.details)

# 객체 생성
student1 = Student("하성운", 1, 1, {"gender" : "male", "score1" : 95, "score2" : 88})
student2 = Student("박보검", 2, 2, {"gender" : "female", "score1" : 75, "score2" : 68})
student3 = Student("김수현", 3, 3, {"gender" : "male", "score1" : 99, "score2" : 89})

# __dict__ : 클래스 인스턴스 값 확인 시 사용
print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)

# 생성된 클래스를 리스트에 담기
student_list = []
student_list.append(student1)
student_list.append(student2)
student_list.append(student3)
print()
print(student_list)   # <__main__.Student object at 0x000001FA99646310>, <__main__.Student object at 0x000001FA99678FA0>, <__main__.Student object at 0x000001FA99688400>
print()
for stu in student_list:
    print(stu)
