class Solution(object):
    MODULO_AMT = 10 ** 9 + 7
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        len1, len2 = len(nums1), len(nums2)
        sum1, sum2 = 0, 0
        i, j = 0, 0
        ans = 0
        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                ans += max(sum1, sum2) + nums1[i]
                ans % self.MODULO_AMT
                sum1 = 0
                sum2 = 0
                i += 1
                j += 1
        while i < len1:
            sum1 += nums1[i]
            i += 1
        while j < len2:
            sum2 += nums2[j]
            j += 1

        ans += max(sum1, sum2)
        return ans % self.MODULO_AMT
                
        