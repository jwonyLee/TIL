# https://www.acmicpc.net/problem/10820
# 문자열 분석
import sys

while True:
    word = sys.stdin.readline()
    if not(word):
        break
    cnt = [0 for _ in range(0, 4)]

    for w in word:
        if w.islower():
            cnt[0] += 1
        elif w.isupper():
            cnt[1] += 1
        elif w.isdigit():
            cnt[2] += 1
        elif w == " ":
            cnt[3] += 1

    print(" ".join(map(str, cnt)))