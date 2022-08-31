class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        start = end = 0
        window = set()
        longest = 0
        
        while start < n:
            if s[start] not in window:
                window.add(s[start])
                start += 1
            else:
                window.remove(s[end])
                end += 1
            longest = max(longest, start - end)
        return longest
            
        