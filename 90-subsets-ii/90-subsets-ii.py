class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        def dfs(start_index, subset):
            if start_index == n:
                result.append(subset[:])
                return
            subset.append(nums[start_index])
            dfs(start_index+1, subset)
            subset.pop()
            while start_index + 1 < n and nums[start_index] == nums[start_index+1]:
                start_index += 1
            dfs(start_index+1, subset)
            
        dfs(0, [])
        return result
        