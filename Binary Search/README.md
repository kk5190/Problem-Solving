# Binary Search

Binary search is an efficient array search algorithm. It works by narrowing down the search range by half each time. 

***Given a sorted array of integers and an integer called target, find the element that equals the target and return its index. If the element is not found, return -1.***

The key observation here is that the array is sorted. We pick a random element in the array and compare it to the target.

- If we happen to pick the element that equals the target (how lucky!), then bingo. We don't need to do any more work; return its index.
- If the element is smaller than the target, then we know the target cannot be found in the section to the left of the current element since everything to the left is even smaller. So we discard the current element and everything on the left from the search range.
- If the element is larger than the target, then we know the target cannot be found in the section to the right of the current element since everything to the right is even larger. So we discard the current element and everything on the right from the search range.

We repeat this process until we find the target. Instead of picking a random element, we always pick the **middle** element in the current search range. This way, we can discard half of the options and shrink the search range by half each time. **This gives us O(log(N)) runtime.**

```python
def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:  # <= because left and right could point to the same element, < would miss it
        mid = (left + right) // 2 # double slash for integer division in python 3, we don't have to worry about integer `left + right` overflow since python integers can be arbitrarily large
        # found target, return its index
        if arr[mid] == target:
            return mid
        # middle less than target, discard left half by making left search boundary `mid + 1`
        if arr[mid] < target:
            left = mid + 1
        # middle greater than target, discard right half by making right search boundary `mid - 1`
        else:
            right = mid - 1
    return -1 # if we get here we didn't hit above return so we didn't find target

```