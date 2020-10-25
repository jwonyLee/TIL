# https://www.acmicpc.net/problem/1427
# 소트인사이드
import sys

arr = list(sys.stdin.readline().strip())
arr.sort(reverse=True)
print(''.join(map(str, arr)))