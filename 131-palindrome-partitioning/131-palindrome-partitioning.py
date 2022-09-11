class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        
        def is_palindrome(word):
            return word == word[::-1]
        
        def dfs(start, path):
            if start == n:
                ans.append(path[:])
                return
            
            for i in range(start+1, n+1):
                prefix = s[start:i]
                if is_palindrome(prefix):
                    dfs(i, path + [prefix])
        dfs(0, [])
        return ans
        