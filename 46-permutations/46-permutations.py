class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(start_index, path, used, result):
            if start_index == len(nums):
                result.append(path[:])
                return
            for index , num in enumerate(nums):
                if used[index]:
                    continue
                path.append(num)
                used[index] = True
                dfs(start_index + 1, path, used, result)
                path.pop()
                used[index] = False
                
        result = []
        used = [False] * len(nums)
        dfs(0, [], used, result)
        return result
        