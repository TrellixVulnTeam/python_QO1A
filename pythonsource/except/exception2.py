# 예외 처리
# try ~ except
# try ~ except ~ else
# try ~ except ~ else ~ finally

# try 예외발생코드 except 예외처리코드
# try 예외발생코드 finally 예외와 상관없이 처리 코드
# try 예외발생코드 except 예외처리코드 else 예외가 안나는 경우 코드
# try 예외발생코드 except 예외처리코드 else 예외가 안나는 경우 코드 finally 예외와 상관없이 처리 코드

#%%
name = ["Kim", "Lee", "Park"]
try:
    z = "Let"
    x = name.index(z)  # ValueError 발생 부분
    print("{} Found it! in name {}".format(z, x + 1))
except:
    print("오류발생")

#%%
# ValueError
try:
    number_input = int(input("정수입력 >> "))
    print("원 반지름 :", number_input)
    print("원 둘레 :", 2 * 3.14 * number_input)
    print("원 넓이 :", 3.14 * number_input * number_input)
except ValueError:
    print("입력값을 확인해 주세요")

#%%
# KeyError
try:
    dict = {"name":"Ha","age":27, "city":"seoul"}
    print(dict["hobby"]) # KeyError: 'hobby'
except KeyError:
    print("찾으려는 키가 없습니다.")

#%%
# try ~ except ~ else
name = ["Kim", "Lee", "Park"]
try:
    # z = "Let"
    z = "Kim"
    x = name.index(z)  # ValueError 발생 부분
    print("{} Found it! in name {}".format(z, x + 1))
except ValueError:
    print("오류발생")
else: # 예외가 없을 때 실행
    print("종료")

#%%
# try ~ except ~ else
name = ["Kim", "Lee", "Park"]
try:
    # z = "Let"
    z = "Kim"
    x = name.index(z)  # ValueError 발생 부분
    print("{} Found it! in name {}".format(z, x + 1))
except Exception: # 어떤 예외가 나는지 모를 때
    print("오류발생")
else: # 예외가 없을 때 실행
    print("종료")

#%%
# try ~ except ~ else ~ finally
name = ["Kim", "Lee", "Park"]
try:
    # z = "Let"
    z = "Kim"
    x = name.index(z)  # ValueError 발생 부분
    print("{} Found it! in name {}".format(z, x + 1))
except Exception: # 어떤 예외가 나는지 모를 때
    print("오류발생")
else: # 예외가 없을 때 실행
    print("종료")
finally:
    print("무조건 실행")

#%%
# try ~ finally
try:
    print("Try")
finally:
    print("Finally")

#%%
# try ~ except(여러개) ~ else ~ finally
name = ["Kim", "Lee", "Park"]
try:
    z = "Let"
    # z = "Kim"
    x = name.index(z)  # ValueError 발생 부분
    print("{} Found it! in name {}".format(z, x + 1))
except ValueError:
    pass
except IndexError:
    pass
except Exception: # 어떤 예외가 나는지 모를 때
    print("오류발생")
else: # 예외가 없을 때 실행
    print("종료")
finally:
    print("무조건 실행")

#%%
# print(e)
try:
    number_input = int(input("정수입력"))
except Exception as e:
    print(e)  # 에러메시지를 언어 자체가 제공하는 걸로 출력

#%%
# raise : 에러 강제 발생
try:
    a = "333"
    if a == "Kim":
        print("정답")
    else:
        raise ValueError  # ValueError 강제발생
except ValueError as v:
    print(v)
else:
    print("종료")

#%%
numbers = [52, 273, 32, 103, 90, 1, 10, 275]

# 32라는 값이 있는지 확인한 후 위치 출력
# 10000이라는 값이 있는지 확인 후 위치 출력
# 값이 없는 경우 나올 수 있는 예외 처리하기
# 값이 없는 경우 출력문 => "리스트 내부에 없는 값입니다."
try:
    print("{}는 {} 위치에 있음".format(32, numbers.index(32)))
    print("{}는 {} 위치에 있음".format(10000, numbers.index(10000)))
except ValueError:
    print("리스트 내부에 없는 값입니다.")
    