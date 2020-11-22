# https://www.acmicpc.net/problem/10808
# 알파벳 개수
import sys

word = sys.stdin.readline().strip()
cnt = [0 for _ in range(0, 26)]

for w in word:
    cnt[ord(w) - 97] += 1

print(" ".join(map(str, cnt)))