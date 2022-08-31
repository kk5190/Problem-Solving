# Intution

The problem description asks us to do it in-place without extra data structure. There are only a couple of things we can do under these constraints - linear traversal or binary search.

We use slow and fast pointers. The fast one moves one element at a time and
- if the current element is 0, do nothing
- if the current element is non-0, swap its element with the slow pointer's element and move the slow pointer

The slow pointer always points to the next 0 if there is one.

The order of non-0 elements is preserved because the early one always gets swapped to the early 0s.
