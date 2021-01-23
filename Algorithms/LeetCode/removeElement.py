# https://leetcode.com/problems/remove-element/
# Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        delete = []
        for i, e in enumerate(nums):
            if e == val:
                delete.append(i)
        for d in reversed(delete):
            nums.pop(d)
        return len(nums)