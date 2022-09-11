class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(nums, start_index, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return
            
            for i in range(start_index, len(nums)):
                num = nums[i]
                if remaining - num < 0:
                    continue
                dfs(nums, i, remaining - num, path + [num])
            
        dfs(candidates, 0, target, [])
        return res
        