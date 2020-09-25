class Account:
    """
    은행계좌 클래스
    계좌번호, 이름, 잔액을 받아서 객체 생성
    입금 / 출금 기능의 메소드 구현
    """
    def __init__(self, accountNo, name, balance):
        self.accountNo = accountNo
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def desposit(self, amount):
        self.balance += amount
        return self.balance
    
    def __str__(self):
        return "{} : 잔액 {}".format(self.name, self.balance)

user1 = Account("111-22-3333", "문상태", 100000)
user2 = Account("222-33-4444", "문강태", 200000)

user1.desposit(100000)
user1.withdraw(50000)
print(user1)

user2.desposit(100000)
user2.withdraw(50000)
print(user2)


