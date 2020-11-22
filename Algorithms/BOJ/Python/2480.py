# https://www.acmicpc.net/problem/2480
# 주사위 세개
import sys

a, b, c = map(int, sys.stdin.readline().split())

if a == b and a == c: # 같은 눈이 3개가 나온 경우
    print(10000 + (a * 1000))
elif a == b or a == c or b == c: # 같은 눈이 2개만 나온 경우
    if a == b or a == c:
        print(1000 + (a * 100))
    else:
        print(1000 + (c * 100))
else: # 모두 다른 눈이 나오는 경우
    print(max(a, b, c)*100)