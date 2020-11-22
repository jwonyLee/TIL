# https://www.acmicpc.net/problem/1316
# 그룹 단어 체커
import sys

def checkBool(arr):
    for value in arr.values():
        if not value:
            return False
    return True

result = 0
n = int(sys.stdin.readline().strip())

for i in range(0, n):
    word = sys.stdin.readline().strip()
    dict = {}
    for j in range(0, len(word)):
        if word[j] in dict:
            if word[j-1] != word[j]:
                dict[word[j]] = False
        else:
            dict[word[j]] = True

    if checkBool(dict):
        result += 1

print(result)