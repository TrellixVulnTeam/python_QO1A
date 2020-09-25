# 사용자 정의 예외
class CustomException(Exception):
    def __init__(self):
        super().__init__(self)
        print("사용자 정의 예외")

    def __str__(self):
        return "오류 발생"

raise CustomException
