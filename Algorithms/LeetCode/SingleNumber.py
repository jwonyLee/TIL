# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = dict()
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        return [key for key, value in dic.items() if value == 1][0]