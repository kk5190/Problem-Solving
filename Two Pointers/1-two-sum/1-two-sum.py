class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        seen = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in seen:
                ans = [seen[diff], index]
            seen[value] = index
        return ans
            
        