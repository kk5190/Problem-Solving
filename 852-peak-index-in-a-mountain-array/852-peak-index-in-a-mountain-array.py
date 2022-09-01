class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        start, end = 0, len(arr) - 1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] > arr[mid+1]:
                ans = mid
                end = mid - 1
            else:
                start = start + 1
        return ans
                
        