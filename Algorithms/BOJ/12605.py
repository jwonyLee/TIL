# https://www.acmicpc.net/problem/12605
# 단어순서 뒤집기
import sys

n = int(sys.stdin.readline())

for i in range(n):
    word = sys.stdin.readline().split()
    print("Case #%d: " % (i+1) ,end="")
    for _ in range(len(word)):
        print(word.pop(), end=" ")
    print()