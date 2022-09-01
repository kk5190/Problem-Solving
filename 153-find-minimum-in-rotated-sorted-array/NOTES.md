# Intution
At first glance, it seems that there's no way to do it in less than linear time. The array is not sorted.

But remember binary search can work beyond sorted arrays, as long as there is a binary decision we can use to shrink the search range.

Notice the numbers are divided into two sections: numbers larger than the last element of the array and numbers smaller than it. The minimum element is at the boundary between the two sections.

We can apply a filter of < the last element and get the boolean array that characterizes the two sections.

**Time Complexity: O(log(n))**
