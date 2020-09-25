# 클래스 상속
class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

class Sedan(Car):
    seatNum = 0
    def getSeatNum(self):
        return self.seatNum

class Truck(Car):
    capacity = 0
    def getCapacity(self):
        return self.capacity

sedan, truck = Sedan(), Truck()

sedan.upSpeed(100)
truck.upSpeed(80)

sedan.seatNum = 5
truck.capacity = 50

print("승용차의 속도는 {}km, 좌석수는 {}개".format(sedan.speed, sedan.getSeatNum()))
print("트럭의 속도는 {}km, 총 중량은 {}톤".format(truck.speed, truck.getCapacity()))
