class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 1, n
        while start <= end:
            mid = (start + end) // 2
            totalCoins = int(mid * (mid+1) / 2)
            if totalCoins == n:
                return mid
            elif totalCoins < n:
                start = mid + 1
            else:
                end = mid -1
        return end
                
        