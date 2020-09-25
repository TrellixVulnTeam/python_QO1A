class Car:
    """
    Car Class
    Author : Jeong
    Date : 2020.08.13
    Description : Class 생성 / 인자 있는 생성자
    """
    car_count = 0

    # 인스턴스 변수 __init__ 생성자 안에 넣기
    def __init__(self, color="black", speed=0):
        self.color = color
        self.speed = speed
        Car.car_count += 1

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value
    def __del__(self):
        Car.car_count -= 1

# 객체 생성
myCar1 = Car(30)
myCar2 = Car("Blue")
myCar3 = Car("Red", 50)

myCar1.upSpeed(20)
print("자동차1의 색상은 {}이며, 현재 속도는 {:3d}km".format(myCar1.color, myCar1.speed))
myCar2.upSpeed(30)
print("자동차2의 색상은 {}이며, 현재 속도는 {:3d}km".format(myCar2.color, myCar2.speed))
myCar3.upSpeed(40)
print("자동차3의 색상은 {}이며, 현재 속도는 {:3d}km".format(myCar3.color, myCar3.speed))

print()
print("myCar1 주소 :", id(myCar1))
print("myCar2 주소 :", id(myCar2))
print("myCar3 주소 :", id(myCar3))

print()
print(Car.__doc__)

print()
print("생산된 총 자동차 수 : {}".format(Car.car_count))