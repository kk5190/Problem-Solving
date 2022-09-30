class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
        
        for i, cur in enumerate(nums):
            while stack and stack[-1][0] < cur:
                value, index = stack.pop()
                result [index] = cur
            stack.append((cur, i))
        
        for cur in nums:
            while cur > stack[-1][0]:
                value, index = stack.pop()
                result[index] = cur
        return result
                
        