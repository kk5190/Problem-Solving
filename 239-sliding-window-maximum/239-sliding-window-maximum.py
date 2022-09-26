class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        
        for i, cur in enumerate(nums):
            while q and nums[q[-1]] <= cur:
                q.pop()
            q.append(i)
            
            if q[0] == i - k:
                q.popleft()
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans
        
        