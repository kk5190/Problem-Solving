from heapq import heapify, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(matrix[0][0], 0, 0)]
        column_top = [0] * n
        row_first = [0] * n
        while k > 1:
            k -= 1
            min_val, row, column = heappop(heap)
            row_first[row] = column + 1
            if column + 1 < n and column_top[column + 1] == row:
                heappush(heap, (matrix[row][column + 1], row, column + 1))
            column_top[column] = row + 1
            
            if row + 1 < n and row_first[row + 1] == column:
                heappush(heap, (matrix[row + 1][column], row + 1, column))
        return heap[0][0]
        