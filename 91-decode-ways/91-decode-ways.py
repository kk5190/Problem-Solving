class Solution:
    def numDecodings(self, s: str) -> int:
        prefixes = [str(i) for i in range(1, 27)]
        def dfs(start_index, memo):
            if start_index in memo:
                return memo[start_index]
            
            if start_index == len(s):
                return 1
            
            ways = 0
            remaining = s[start_index:]
            for prefix in prefixes:
                if remaining.startswith(prefix):
                    ways += dfs(start_index + len(prefix), memo)
            
            memo[start_index] = ways
            return ways
        return dfs(0, {})
        