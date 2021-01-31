# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/
# Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n+1):
            if i not in nums:
                return i