# https://www.acmicpc.net/problem/1157
# 단어 공부

import sys
answer = ''
max = -1
dict = {}
s = sys.stdin.readline().strip().lower()

for i in s:
    dict[i] = dict.get(i, 0) + 1
for k, v in dict.items():
    if max < v:
        max = v
        answer = k
    elif max == v:
        answer = '?'

print(answer.upper())