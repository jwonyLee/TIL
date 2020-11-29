# https://www.acmicpc.net/problem/1919
# 애너그램 만들기
import sys

word1 = sys.stdin.readline().strip()
word2 = sys.stdin.readline().strip()
cnt1 = [0 for _ in range(26)]
cnt2 = [0 for _ in range(26)]

for w in word1:
    cnt1[ord(w) - 97] += 1
for w in word2:
    cnt2[ord(w) - 97] += 1
cnt = 0
for c1, c2 in zip(cnt1, cnt2):
    cnt += abs(c1 - c2)

print(cnt)