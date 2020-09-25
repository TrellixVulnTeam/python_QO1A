class FourCal:
    """
    FourCal
    사칙연산 기능을 가지고 있는 계산기
    두 개의 정수를 받아 사칙 연산을 한 후 연산 결과를 리턴하는
    4개의 메소드를 작성한다.
    생성자는 두 개의 변수를 초기화하는 형태로 작성하기
    """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def multi(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

num1, num2 = 10, 5
four1 = FourCal(num1, num2)

print("{} + {} = {}".format(num1, num2, four1.sum()))
print("{} - {} = {}".format(num1, num2, four1.sub()))
print("{} * {} = {}".format(num1, num2, four1.multi()))
print("{} / {} = {}".format(num1, num2, four1.div()))
