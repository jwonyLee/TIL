# https://www.acmicpc.net/problem/2587
# 대표값2
import sys

nums = []
for _ in range(5):
    nums.append(int(sys.stdin.readline()))
nums.sort()

print(int(sum(nums)/len(nums)))
print(nums[int(len(nums)/2)])