# https://www.acmicpc.net/problem/10799
# 쇠막대기
import sys
string = sys.stdin.readline().strip()
s = []
cnt = 0
for i, c in enumerate(string):
    if c == "(":
        s.append(c)
    else:
        s.pop()
        if string[i-1] == "(": 
            cnt += len(s)
        else:
            cnt += 1
print(cnt)