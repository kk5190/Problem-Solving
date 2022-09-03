# Intution

The binary decision we have to make when we look at an element is

- if the element is not BadVersion, we discard everything to the left and the current element itself.
- if the element is BadVersion, the current element could be the first BadVersion although there may be other BadVersion to the left. We discard everything to the right but what about the current element?

We can either keep the current element in the range or record it somewhere and then discard it. Here we choose the latter.

We keep a variable `ans` that represents the leftmost BadVersion's index currently recorded. If the current element is BadVersion, then we update `ans` with its index and discard everything to the right including the current element itself since its index has been recorded by the variable.

**Time Complexity: O(log(n))**
