# https://www.acmicpc.net/problem/11720
import sys

n = int(sys.stdin.readline())
number = sys.stdin.readline().strip()
result = 0

for s in number:
    result += int(s)

print(result)
