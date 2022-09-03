# Intution

The peak element is always larger than the next element. So, the binary decision we have to make when we look at an element is

- if the element is less or equal than the next element, we discard everything to the left.
- if the element is greater, the current element could be the Peak Element although there may be other Peak elements to the left. We discard everything to the right but what about the current element?
We can either keep the current element in the range or record it somewhere and then discard it. Here we choose the latter.

We keep a variable `ans` that represents the leftmost Peak Elements's index currently recorded. If the current element is Peak Element, then we update `ans` with its index and discard everything to the right including the current element itself since its index has been recorded by the variable.

Time Complexity: O(log(n))
