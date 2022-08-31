# Intuition
If it was an array, then we can get its length and middle element trivially. For a linked list, we have to traverse it to find its length l. We can find l by traversing the list once and then find the middle element by traversing it again and stop on the l/2th element.

Is there any way to traverse only once? We can use two pointers
- a fast pointer that moves 2 nodes at a time and
- a slow pointer that moves 1 node at a time

Since the speed of the fast pointer is 2x of the slow pointer, by the time the fast pointer reaches the end the slow pointer should be at the eexact middle of the list.

**Time Complexity: O(n)**
