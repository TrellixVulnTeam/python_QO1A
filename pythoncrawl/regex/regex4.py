import re

# 정규식 패턴
# [] : 괄호 안에 들어있는 문자 찾기
# [ - ] : 괄호 안에 문자를 범위 형태로 지정
# [^ ] : 괄호 안에 쓰여진 문자 제외

pattern = re.compile("[abcdefgABCDEFG]")
print("[] : 괄호 안에 들어있는 문자 찾기")
print(pattern.search("a1234"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("z1234"))  # None

print()
pattern = re.compile("[a-gA-G]")
print("[ - ] : 괄호 안에 문자를 범위 형태로 지정")
print(pattern.search("a1234"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("z1234"))  # None

pattern = re.compile("[a-gA-G0-9]")  # a-gA-G --> 대소문자 모두 대응 가능
print(pattern.search("1234---"))  # <re.Match object; span=(0, 1), match='1'>
print(pattern.search("--------!@#$%^&*------"))  # None
print(pattern.search("abcdefg"))  # <re.Match object; span=(0, 1), match='a'>

print()
pattern = re.compile("[^a-zA-Z0-9]")
print("[^ ] : 괄호 안에 쓰여진 문자 제외")
print(pattern.search("1234---"))  # <re.Match object; span=(4, 5), match='-'>
print(pattern.search("--------!@#$%^&*------"))  # <re.Match object; span=(0, 1), match='-'>
print(pattern.search("abcdefg"))  # None

print()
pattern = re.compile("[가-힣]")  # 자음, 모음 따로 지정도 가능
print("한글 찾기")
print(pattern.search("나"))  # <re.Match object; span=(0, 1), match='나'>
