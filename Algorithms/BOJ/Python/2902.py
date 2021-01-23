# https://www.acmicpc.net/problem/2902
# KMP는 왜 KMP일까?
import sys
text = sys.stdin.readline().strip().split("-")
answer = ""
for word in text:
    answer += word[0]
print(answer)
