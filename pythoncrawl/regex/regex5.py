import re

# 정규식
# sub() : 찾고 바꾸기
# match() : 문자열 처음부터 정규식과 매칭되는 패턴을 찾아서 리턴   ---> 처음이 다르면 끝
# search() : 문자열 전체를 검색해서 정규식과 매칭되는 패턴을 찾아서 리턴   ---> 전체 중에 일치하는 부분 찾아옴

pattern = re.compile("[a-z]+")  # + : 최대한 많이 찾을 수 있도록
matched = pattern.match("Dave") # 모두 소문자인걸 찾고싶을 때
print("match() : ", matched)    # match() :  None
searched = pattern.search("Dave") # 소문자가 들어있기만하면될 때
print("search() : ", searched)  # search() :  <re.Match object; span=(1, 4), match='ave'>

print()
print("*** 찾고 바꾸기 ***")
string = "DDA D1A DDA DA"
# re.sub(패턴, 바꿀문자열, "원본문자열")
result = re.sub("D.A", "Dave", string)
print(result)  # Dave Dave Dave DA

pattern = re.compile("D[.]A")
result = re.sub(pattern, "Dave", string)
print(result)  # DDA D1A DDA DA

# findall() : 정규표현식과 매칭되는 모든 문자열을 리스트 객체로 리턴
pattern = re.compile("[a-z]+")
print(pattern.findall("Game of Life in Python"))
pattern = re.compile("[A-Za-z]+")
print(pattern.findall("Game of Life in Python"))

# split() : 찾은 정규표현식 패턴 문자열을 기준으로 문자열 분리
print()
pattern = re.compile(":")
print(pattern.split("python:java"))
