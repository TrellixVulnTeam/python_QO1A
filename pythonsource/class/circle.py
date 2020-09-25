import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius   # __ 를 붙이면 private
    
    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_circleArea(self):
        return math.pi * (self.__radius ** 2)

    def get_redius(self): # getter
        return self.__radius

    def set_redius(self, value): # setter
        self.__radius = value


circle = Circle(10)
print("원의 둘레", circle.get_circumference())
print("원의 면적", circle.get_circleArea())

print(circle.set_redius(15))
print("원의 둘레", circle.get_circumference())
print("원의 면적", circle.get_circleArea())
print(circle.get_redius())
