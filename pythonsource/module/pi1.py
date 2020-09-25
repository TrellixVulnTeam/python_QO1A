PI = 3.141592


def number_input():
    output = float(input("숫자입력 > "))
    return output


def get_circumference(radius):
    return 2 * PI * radius


def get_circleArea(radius):
    return PI * radius * radius
