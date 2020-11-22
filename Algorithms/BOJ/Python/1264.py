# https://www.acmicpc.net/problem/1264
# 모음의 개수
import sys

word = sys.stdin.readline().strip()

while word != "#":
    word = word.lower()
    cnt = 0

    for w in word:
        if w in "aioue":
            cnt += 1
    
    print(cnt)
    word = sys.stdin.readline().strip()