class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0: # 짝수
            mid = int(len(nums) / 2)
            return (nums[mid - 1] + nums[mid]) / 2
        else: # 홀수
            return nums[int(len(nums) / 2)]