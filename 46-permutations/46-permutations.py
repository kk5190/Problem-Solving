class Solution(object):
    def dfs(self, path, used, res, nums):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i , num in enumerate(nums):
                if used[i]:
                    continue
                path.append(num)
                used[i] = True
                self.dfs(path, used, res, nums)
                path.pop()
                used[i] = False
                
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs([], [False] * len(nums), res, nums)
        return res
        