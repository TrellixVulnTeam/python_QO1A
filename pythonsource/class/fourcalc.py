class FourCal:
    """
    FourCal
    사칙연산 기능을 가지고 있는 계산기
    두 개의 정수를 받아 사칙 연산을 한 후 연산 결과를 리턴하는
    4개의 메소드를 작성한다.
    생성자는 두 개의 변수를 초기화하는 형태로 작성하기
    """
    @classmethod
    def plus(num1, num2):
        print("%s + %s =" % (num1, num2, num1 + num2))
    @classmethod
    def minus(num1, num2):
        print("%s - %s =" % (num1, num2, num1 - num2))
    @classmethod
    def cal0(num1, num2):
        print("%s * %s =" % (num1, num2, num1 * num2))
    @classmethod
    def cal00(num1, num2):
        print("%s / %s =" % (num1, num2, num1 / num2))
 
num1 = input("첫번째 숫자를 입력하세요")
num2 = input("두번째 숫자를 입력하세요")
op = input("연산자를 입력하세요")

if op == "+":
    FourCal.plus(num1, num2)
elif op == "-":
    FourCal.plus(num1, num2)
elif op == "*":
    FourCal.plus(num1, num2)
elif op == "/":
    FourCal.plus(num1, num2)
