class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        start , end = 0, 0
        ans = 0
        n = len(colors)
        while start < n and end < n:
            color_max, color_total = 0, 0
            while end < n and colors[start] == colors[end]:
                color_max = max(color_max, neededTime[end])
                color_total += neededTime[end]
                end += 1
            start = end
            ans += (color_total - color_max)
        return ans
        
        