# https://www.acmicpc.net/problem/10809
# 알파벳 찾기

import sys

S = sys.stdin.readline().strip()
alpha = [-1 for i in range(26)]

for s in range(len(S)):
    idx = 122 - ord(S[s])
    if alpha[idx] == -1:
        alpha[idx] = s

for i in list(reversed(alpha)):
    print(i, end=' ')