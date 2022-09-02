# Intutiton

At minimum, the truck's capacity has to be >= max(weights) to be able to carry the biggest package.

At maximum, if our truck capacity is sum(weights), then it'd take only 1 day to ship.

Since we want to ship within d days, the optimal truck capacity somewhere in between.

We know how to find if a truck capacity is feasible or not - we simply loop through the weights and see if we can ship it within d days.

** Time complexity: O(n log n) **

In our solution, setting the initial min_ptr and max_ptr values takes O(n) to find out the maximum value and the sum of weights. Then, performing binary search is O(log n), and the helper function feasible() that is called inside the binary search loop is O(n). Overall, the binary search takes O(n log n), which is more significant than O(n), so the time complexity of our solution is O(n log n).
