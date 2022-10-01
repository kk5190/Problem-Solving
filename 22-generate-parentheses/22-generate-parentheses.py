class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(start_index, path, open_count, close_count, res):
            if start_index == 2 * n:
                res.append(''.join(path))
                return
            if open_count < n:
                path.append('(')
                dfs(start_index + 1, path, open_count + 1, close_count, res)
                path.pop()
            
            if close_count < open_count:
                path.append(')')
                dfs(start_index + 1, path, open_count, close_count + 1, res)
                path.pop()
        ans = []
        dfs(0, [], 0, 0, ans)
        return ans