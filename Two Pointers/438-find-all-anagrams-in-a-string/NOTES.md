# Intution

This is a classical sliding window problem. The sliding window is maintained at the size of **p**, and we keep track of the number of each type of characters inside the window in a hashmap. Every cycle, we move the window to the right, pushing the rightmost character while popping the leftmost character. We check that at any given time, if the content of the set matches the character count of check, by definition, that substring is an anagram, and we can insert the index into the resulting list.

**Time Complexity: O(n)**
