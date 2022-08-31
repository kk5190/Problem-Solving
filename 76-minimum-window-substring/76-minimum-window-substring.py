class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "":
            return ""

        checkCount, window = {}, {}

        for c in t:
            checkCount[c] = 1 + checkCount.get(c, 0)

        have, need = 0, len(checkCount)
        res, resLen = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in checkCount and window[c] == checkCount[c]:
                have += 1
            
            while have == need:
                #update result
                if (r - l +1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                #pop from left of window
                window[s[l]] -= 1
                if s[l] in checkCount and window[s[l]] < checkCount[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        