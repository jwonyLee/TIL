# https://www.acmicpc.net/problem/5622
# 다이얼
import sys

dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

number = list(sys.stdin.readline().strip())
time = 0

for n in number:
    for d in range(0, len(dial)):
        if n in dial[d]:
            time += d + 3
print(time)