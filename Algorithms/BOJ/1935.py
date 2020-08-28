# https://www.acmicpc.net/problem/1935
# 후위 표기식2
import sys

n = int(sys.stdin.readline())
formula = sys.stdin.readline().strip()
num = [int(sys.stdin.readline()) for _ in range(0, n)]
operator = ["+", "-", "*", "/"]
s = []

for f in formula:
    if not f in operator:
        s.append(num[ord(f) - 65])
    else:
        if f == "+":
            s.append(s.pop() + s.pop())
        elif f == "-":
            back = s.pop()
            front = s.pop()
            s.append(front - back)
        elif f == "*":
            s.append(s.pop() * s.pop())
        else:
            back = s.pop()
            front = s.pop()
            s.append(front / back)

print("%.2f" % float(s[0]))