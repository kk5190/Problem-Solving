class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= nums[-1]:
                end = mid - 1
            else:
                start = mid + 1
        return nums[start]
        