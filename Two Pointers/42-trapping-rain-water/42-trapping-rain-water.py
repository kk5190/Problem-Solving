class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left_heights = [0] * n # to track the left heights
        right_heights = [0] * n # to track the right heights
        
        #find the max left
        max_left_height = 0
        for i in range(n):
            left_heights[i] = max_left_height
            max_left_height = max(height[i], max_left_height)
        
        #find the max right
        max_right_height = 0
        for i in reversed(range(n)):
            right_heights[i] = max_right_height
            max_right_height = max(height[i], max_right_height)
        
        total_water = 0
        for i in range(n):
            wall = height[i]
            lowest_height = min(left_heights[i], right_heights[i])
            if lowest_height > wall:
                total_water += lowest_height - wall
        return total_water
        
        