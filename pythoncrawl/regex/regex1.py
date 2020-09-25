import re

# 정규식 패턴 생성
pattern = re.compile("D.A")  # . : 어떤 문자라도 매치  // D로 시작하고 가운데 아무 문자나 하나 오고 뒤가 A로 끝나는 거 찾아줭

# search : 패턴이 매칭되는 여부 확인 / 전체문자열을 검색해서 일치하는 영역을 찾아줌
result = pattern.search("DAA")
print(result)  # <re.Match object; span=(0, 3), match='DAA'>

result = pattern.search("D1A")
print(result)  # <re.Match object; span=(0, 3), match='D1A'>

result = pattern.search("D00A")
print(result)  # None

result = pattern.search("DA")
print(result)  # None

result = pattern.search("d0A")
print(result)  # None

result = pattern.search("d0A D1A 0111")
print(result)  # <re.Match object; span=(4, 7), match='D1A'>
