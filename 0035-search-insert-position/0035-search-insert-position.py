class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid - 1
                ans = mid
            else:
                start = mid + 1
                ans = mid + 1
        return ans
            
                
        