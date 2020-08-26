# https://www.acmicpc.net/problem/10818
# 최소, 최대
import sys

n = sys.stdin.readline()
element = list(map(int, sys.stdin.readline().strip().split(" ")))
print(min(element), max(element))