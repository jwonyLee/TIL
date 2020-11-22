# https://www.acmicpc.net/problem/10804
# 카드 역배치
import sys

cards = [i for i in range(0, 20+1)]

for _ in range(10):
    start, end = map(int, sys.stdin.readline().split())
    cards[start:end+1] = cards[start:end+1][::-1]

print(' '.join(map(str, cards[1:])))