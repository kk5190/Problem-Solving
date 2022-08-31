# Intuition

This is a straightforward two-pointer problem. We have two pointers l and r, starting from the leftmost and rightmost positions and moving towards each other. At each step,

- if the elements they point to are the same, then we move each pointer one position towards each other;
- otherwise, the string is not a palindrome.

Note that the problem asks us to ignore all non-alphanumeric characters. So any time we see one we have to skip it by incrementing one position only for the corresponding pointer.
