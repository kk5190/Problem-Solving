# Intution

For simplicity, we call numbers that appears multiple times "teleporters". Because both arrays are ordered and distinct, teleporter number must appear in both array exactly once, and each teleporter in both arrays must be ordered in the same way.

Consider the interval between two teleporters. If there are no number between these two numbers that appear in both array, then in those steps you can only go forward. Therefore, the score in that section would be the sum of the subarray in that section.

Furthermore, regardless where you start, it does not affect the choice whether to go top or go bottom in that section. If you start from the top array, you can go left to continue the top array, and teleport to the bottom array. The same goes for if you start from the bottom array. In that case, to maximize the score, we only need to maximize the score of each interval between two teleporters.

Note that the same holds true for numbers before the first teleporter and after the final teleporter, so we can apply the same logic.

For the same implementation, we use two pointers, one for each array. We always move the smaller pointer forward and keep track of the sum of the subsection until both pointers are the same. Then, we find the maximum sum between these two subsections and add them to the result. Repeat this until we finished iterating through both arrays. The time complexity is O(n+m), where n and m are the size of the arrays, respectively.
