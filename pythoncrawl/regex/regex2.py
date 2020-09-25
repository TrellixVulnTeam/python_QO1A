import re

# 정규식
# . : 어떤 문자든 매칭
# ? : 최소 0 ~ 1 / 물음표 앞자리의 문자의 개수를 조절
# * : 최소 0 ~ 무한대
# + : 최소 1 ~ 무한대

pattern = re.compile("D?A")  # D가 0개이거나 1개가 있고 A로 끝나는 거 찾아줘
print("? : 최소 0 ~ 1")
print(pattern.search("A"))   # <re.Match object; span=(0, 1), match='A'>
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(pattern.search("AA"))  # <re.Match object; span=(0, 1), match='A'>   ---> 앞쪽의 A를 찾아온거

print()
pattern = re.compile("D*A")  # D가 0개에서 몇개가 와도 되고 A로 끝나는 거 찾아줘
print("* : 최소 0 ~ 무한대")
print(pattern.search("A"))   # <re.Match object; span=(0, 1), match='A'>
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(pattern.search("DDDDDDDDDDDDA"))  # <re.Match object; span=(0, 13), match='DDDDDDDDDDDDDA'>

print()
pattern = re.compile("D+A")  # D가 최소 1개에서 몇개가 와도 되고 A로 끝나는 거 찾아줘
print("+ : 최소 1 ~ 무한대")
print(pattern.search("A"))   # None
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(pattern.search("DDDDDDDDDDDDA"))  # <re.Match object; span=(0, 13), match='DDDDDDDDDDDDDA'>
