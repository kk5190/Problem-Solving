class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def feasible(weights, max_weight, d):
            req_days = 1
            capacity = max_weight
            i = 0
            n = len(weights)
            while i < n:
                if weights[i] <= capacity:
                    capacity -= weights[i]
                    i += 1
                else:
                    req_days += 1
                    capacity = max_weight
            return req_days <= d

        min_ptr = max(weights)
        max_ptr = sum(weights)
        boundary_index = max_ptr
        while min_ptr <= max_ptr:
            midpoint = (min_ptr + max_ptr) // 2
            if feasible(weights, midpoint, days):
                boundary_index = midpoint
                max_ptr = midpoint - 1
            else:
                min_ptr = midpoint + 1
        return boundary_index