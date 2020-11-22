# https://www.acmicpc.net/problem/2444
# 별 찍기 - 7
import sys

n = int(sys.stdin.readline())
for i in range(2*n-1):
    if n > i:
        print(" "*(n-(i+1)), end="")
        print("*"*(2*i+1))
    else: # 등차수열 공식 참고
        print(" "*(n-(abs(i + (n - 1) * -2)+1)), end="")
        print("*"*(2*(abs(i + (n - 1) * -2))+1))