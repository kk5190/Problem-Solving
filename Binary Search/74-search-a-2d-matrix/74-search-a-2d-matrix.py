class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        top_row, bottom_row = 0, ROWS - 1
        row_to_search = - 1
        
        #Apply binary search to find the row
        #where target can be found
        while top_row <= bottom_row:
            row_to_search = (top_row + bottom_row) // 2
            if target > matrix[row_to_search][-1]:
                top_row = row_to_search + 1
            elif target < matrix[row_to_search][0]:
                bottom_row = row_to_search - 1
            else:
                break
            
        if row_to_search == -1:
            return False
        
        #Apply binary search to find the element
        #on row_to_search
        left, right = 0 , COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row_to_search][mid]:
                left = mid + 1
            elif target < matrix[row_to_search][mid]:
                right = mid - 1
            else:
                return True
        return False
        
        
        