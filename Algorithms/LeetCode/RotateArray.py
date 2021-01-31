# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
# Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, k):
            nums.insert(0, nums.pop())