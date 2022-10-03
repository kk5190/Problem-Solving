class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        previous = 0
        
        for i in range(1, len(colors)):
            if colors[i] != colors[previous]:
                previous = i
            else:
                ans += min(neededTime[i], neededTime[previous])
                if neededTime[previous] < neededTime[i]:
                    previous = i
                
        return ans
        
        