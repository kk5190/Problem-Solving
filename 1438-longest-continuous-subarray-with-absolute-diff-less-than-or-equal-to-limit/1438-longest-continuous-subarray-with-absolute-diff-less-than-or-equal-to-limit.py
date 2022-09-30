class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        min_deque = deque()
        max_deque = deque()
        n = len(nums)
        left = 0
        for right in range(n):
            while min_deque and nums[right] < nums[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(right)
            
            while max_deque and nums[right] > nums[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                left += 1
            ans = max(ans, right -left + 1)
        return ans
            
            
        