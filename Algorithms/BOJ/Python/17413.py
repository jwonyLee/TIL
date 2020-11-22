# https://www.acmicpc.net/problem/17413
# 단어 뒤집기2
import sys
from collections import deque

word = sys.stdin.readline().strip()
stack = deque()

for s in word:
    if s == "<":
        while len(stack) > 0:
            print(stack.pop(), end="")
        stack.append(s)
    elif s == ">":
        stack.append(s)
        while len(stack) > 0:
            print(stack.popleft(), end="")
    elif s == " " and stack[0] != "<":
        while len(stack) > 0:
            print(stack.pop(), end="")
        print(" ", end="")
    else:
        stack.append(s)

while len(stack) > 0:
    print(stack.pop(), end="")
print()