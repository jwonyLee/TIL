# https://www.acmicpc.net/problem/1712
# 손익분기점
# 참조: https://jaemin8852.tistory.com/227
import sys

arr = list(map(int, sys.stdin.readline().strip().split(" ")))

if arr[1] >= arr[2]:
    print(-1)
else:
    print(int(arr[0]/(arr[2] - arr[1])) + 1)