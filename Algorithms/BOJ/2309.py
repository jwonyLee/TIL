# https://www.acmicpc.net/problem/2309
# 일곱 난쟁이
import sys

def find():
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            temp = sum(nums) - nums[i] - nums[j]
            if temp == 100:
                result = [x for x in nums if x not in [nums[i], nums[j]]]
                result.sort()
                return result

nums = []
for _ in range(9):
    nums.append(int(sys.stdin.readline()))

found = find()
for f in found:
    print(f)