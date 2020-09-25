# format() : python3 지원
#            대체될 부분에 {} 표시
print("{} and {}".format("You", "me"))
print("{1} and {0}".format("You", "me"))            # 순서 지정 가능
print("{1} and {0} and {1}".format("You", "me"))    # 중복 설정 가능
print("I eat {0} apples".format(3))                 # print("I eat {} apples".format(3))  
print()

# {} 안에 변수 사용 가능
print("{var1} and {var2}".format(var1="You", var2="me"))
print("I eat {number} apples. so I was sick for {day} days".format(number=10,day=3))
print("I eat {} apples. so I was sick for {day} days".format(10,day=3))                # 직접 설정과 변수 설정 동시에 가능
print()

print("Test1 : {0: 5d}, Price:{1: 4.2f}".format(776,6534.123))


