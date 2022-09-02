class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        min_ptr = max(weights)
        max_ptr = sum(weights)
        boundary_index = max_ptr
        while min_ptr <= max_ptr:
            midpoint = (min_ptr + max_ptr) // 2
            if self.feasible(weights, midpoint, days):
                boundary_index = midpoint
                max_ptr = midpoint - 1
            else:
                min_ptr = midpoint + 1
        return boundary_index
    
    def feasible(self, weights, max_weight, d):
            req_days = 1
            current_weight = 0
            for weight in weights:
                current_weight += weight
                if current_weight > max_weight:
                    req_days += 1
                    current_weight = weight
            return req_days <= d