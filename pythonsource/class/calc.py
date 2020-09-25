class Calculator:
    """
    Calculator Class
    Author : Jeong
    Date : 2020.08.13
    Description : Class 생성 / 생성자
    """
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

# 객체 생성
cal1 = Calculator()
cal2 = Calculator()

print('cal1 : {}'.format(cal1.adder(10)))
print('cal2 : {}'.format(cal2.adder(100)))

