# Intuition

If we could use extra memory, we can easily solve this by going through the list once and using a hashset to record elements we have seen. But we are not allowed extra memory so we have to look at the conditions and see if there's anything we could use. An important condition is that the numbers are sorted, which means the same numbers are next to each other. This means as we go through the list, once we see a number A, we will see all occurrences of A together, and will not see A again after we see B. Using this key observation, we can devise a fast/slow pointer solution.

**Time Complexity: O(n)**
