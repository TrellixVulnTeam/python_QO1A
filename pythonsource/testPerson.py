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
