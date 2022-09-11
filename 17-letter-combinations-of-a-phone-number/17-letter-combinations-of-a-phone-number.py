class Solution:
    

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        self.KEYBOARD = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        def dfs(path, res):
            if len(path) == len(digits):
                res.append(''.join(path))
                return
            next_number = digits[len(path)]
            for letter in self.KEYBOARD[next_number]:
                path.append(letter)
                dfs(path, res)
                path.pop()
                
        res = []
        dfs([], res)
        return res
        