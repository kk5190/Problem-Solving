from heapq import heapify, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heap.append(matrix[i][j])
        
        heapify(heap)
        
        for _ in range(k-1):
            heappop(heap)
        
        return heap[0]
        