# Intuition

The total water the entire structure can hold is the sum of the amount of water each position can hold. The water a position can hold is bound by the lower of the two walls.

Since we already know the height of each position, we just have to find the left and right walls for each position. We should also realize that the height of the wall in a particular direction is decided by the highest height in the direction from the current position.

Therefore, the problem reduces to finding the wall for each cell from each direction. We can easily do this by going through the height array and keeping track of the max height.

**Time Complexity: O(n)**
