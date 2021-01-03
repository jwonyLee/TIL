# https://www.acmicpc.net/problem/11723
# 집합
# 참고: https://www.acmicpc.net/board/view/57656
import sys
s = set()
n = int(sys.stdin.readline().strip())
a = set([str(i) for i in range(1, 21)])
for _ in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == "add":
        s.add(command[1])
    elif command[0] == "remove":
        if s:
            s.remove(command[1])
    elif command[0] == "check":
        if command[1] in s:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if command[1] in s:
            s.remove(command[1])
        else:
            s.add(command[1])
    elif command[0] == "all":
        s = a
    else:
        s = set()