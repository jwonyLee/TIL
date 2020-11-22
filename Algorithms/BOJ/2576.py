# https://www.acmicpc.net/problem/2576
# 홀수
import sys

nums = []
for _ in range(7):
    nums.append(int(sys.stdin.readline()))

odd = [num for num in nums if num % 2 != 0]
if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)