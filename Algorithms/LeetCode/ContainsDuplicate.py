# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
# Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = set(nums)
        if len(dup) == len(nums):
            return False
        else:
            return True
        