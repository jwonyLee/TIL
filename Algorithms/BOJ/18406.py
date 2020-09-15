# https://www.acmicpc.net/problem/18406
# 럭키 스트레이트
import sys

n = sys.stdin.readline().strip()

left = list(map(int, list(n[:int(len(n)/2)])))
right = list(map(int, list(n[int(len(n)/2):])))

if sum(left) == sum(right):
    print("LUCKY") 
else: 
    print("READY")