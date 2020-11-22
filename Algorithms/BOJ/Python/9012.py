# https://www.acmicpc.net/problem/9012
# 괄호
import sys
def isVPS(ps):
    s = 0

    for p in ps:
        if p in "(":
            s += 1
        else:
            s -= 1
            if s < 0:
                return False
    if s == 0:
        return True
    else:
        return False

n = int(sys.stdin.readline())
for _ in range(n):
    ps = sys.stdin.readline().strip()
    if isVPS(ps):
        print("YES")
    else:
        print("NO")
