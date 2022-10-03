class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        previous = 0
        n = len(colors)
        
        for i in range(1, n):
            if colors[i] != colors[previous]:
                previous = i
            else:
                ans += min(neededTime[i], neededTime[previous])
                if neededTime[previous] < neededTime[i]:
                    previous = i
                
        return ans
        
        