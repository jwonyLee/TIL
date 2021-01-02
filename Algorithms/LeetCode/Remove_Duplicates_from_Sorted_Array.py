# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                del nums[i+1]
            i += 1
            print(i, len(nums))
        return len(nums)