from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for node in lists:
            while node:
                heappush(heap, node.val)
                node = node.next
        res = curr = ListNode()
        while heap:
            curr.next = ListNode(heappop(heap))
            curr = curr.next
        return res.next
    
        