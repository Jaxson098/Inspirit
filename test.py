# import re

# def startsWithCaps(string):
#     pattern = r'^\b[A-Z]+\b'
#     return bool(re.search(pattern, string))

# # Example usage
# print(startsWithCaps("HELLO World"))  # True
# print(startsWithCaps("hello world"))       # False
# print(startsWithCaps("Hello World"))       # false
# print(startsWithCaps("hello WORLD"))       # false

from collections import Counter

list = ["Abortion should always Legal", "Abortion should be sometimes legal", "Abortion should be sometimes legal", "Abortion should be illegal", "no opinion about abortion"]

counted = Counter(list)
print(counted.most_common()[0][0])

str(counted.most_common()[0][0])