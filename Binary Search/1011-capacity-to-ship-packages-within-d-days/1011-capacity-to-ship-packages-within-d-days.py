class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        start = max(weights)
        end = sum(weights)
        while start < end:
            mid = (start + end) // 2
            if self.feasible(weights, mid, days):
                end = mid
            else:
                start = mid + 1
        return end
    
    def feasible(self, weights, max_weight, d):
            req_days = 1
            current_weight = 0
            for weight in weights:
                current_weight += weight
                if current_weight > max_weight:
                    req_days += 1
                    current_weight = weight
            return req_days <= d