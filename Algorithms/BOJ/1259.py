# https://www.acmicpc.net/problem/1259
# 팰린드롬수
import sys

n = int(sys.stdin.readline())

while n != 0:
    if str(n) == str(n)[::-1]:
        print("yes")
    else:
        print("no")
    
    n = int(sys.stdin.readline())