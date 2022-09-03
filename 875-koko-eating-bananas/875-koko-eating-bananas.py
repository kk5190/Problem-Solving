class Solution(object):
    def canEat(self, piles, k,  h):
        hours = 0
        for pile in piles:
            hours += ((pile - 1) // k) + 1
        return hours <= h
    
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left , right = 1, max(piles)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if self.canEat(piles, mid, h):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans
                
                
        