class Solution(object):
    
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        MODULO = 10 ** 9 + 7
        i = j = 0
        lenNums1 = len(nums1)
        lenNums2 = len(nums2)
        sumNums1 = 0
        sumNums2 = 0
        ans = 0
        
        while i < lenNums1 or j < lenNums2:
            if i < lenNums1 and j < lenNums2 and nums1[i] == nums2[j]:
                ans += max(sumNums1, sumNums2) + nums1[i]
                ans %= MODULO
                sumNums1 = 0
                sumNums2 = 0
                i += 1
                j += 1
                continue
            if i == lenNums1 or (j != lenNums2 and nums1[i] >nums2[j]):
                sumNums2 += nums2[j]
                j += 1
            else:
                sumNums1 += nums1[i]
                i += 1
        ans += max(sumNums1, sumNums2)
        return ans % MODULO
                
        