# https://www.acmicpc.net/problem/10093
# 숫자
import sys

a, b = map(int, sys.stdin.readline().split())

if a > b:
    a, b = b, a

result = [i for i in range(a+1, b)]
print(len(result))
if result:
    print(' '.join(map(str, result)))