class FourCal:
    def __init__(self):
        super().__init__()

    def sum(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 // num2

# 테스트용 코드 작성
if __name__ == "__main__":
    print(FourCal)
    cal = FourCal()
    print(cal.sum(5, 5))
    print(cal.sub(11, 6))
    print(cal.mul(3, 4))
    print(cal.div(30, 5))
    