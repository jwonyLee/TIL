# https://www.acmicpc.net/problem/1152
# 단어의 개수

import sys

S = sys.stdin.readline().strip().split(' ')
if S[0] == '':
    print(0)
else:
    print(len(S))