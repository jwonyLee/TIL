# https://www.acmicpc.net/problem/11656
# 접미사 배열
import sys

word = list(sys.stdin.readline().strip())
arr = []

lenword = len(word)
for _ in range(0, lenword):
    arr.append("".join(word))
    del word[0]

arr.sort()
for a in arr:
    print(a)