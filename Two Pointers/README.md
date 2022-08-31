# Two Pointers

Two pointers is a common interview technique often used to solve certain problems involving an iterable data structure, such as an array. As the name suggests, this technique uses two (or more) pointers that traverses through the structure. It does not have to be physically using two pointers. As long as the other pointer can be easily calculated from existing values, such as the index of the other pointer, it counts as a two pointer question.

Since "two pointers" is kind of a broad topic, there is no singular way to implement it. Depending on the questions you encounter, you need to implement the answer differently. Generally speaking, a two pointer algorithm has these characteristics:

Two moving pointers, regardless of directions, moving dependently or independently;
A function that utilizes the entries referenced by the two pointers, which relates to the answer in a way;
An easy way of deciding which pointer to move;
A way to process the array when the pointers are moved.
There are a lot of ways to classify two pointer problems. Below are some classifications, although they are in no way exhaustive.

## Classifications
1. Same Directions
1. Opposite Directions
1. Sliding Window
1. Non-array Applications

## Why Use Two Pointers?

Two pointers are helpful because it often offers a more efficient solution than the naive solution. From the examples above, if we use the naive solution and use two loops to iterate through the array, the time complexity is often O(n^2), which is often not enough. If we use two pointers for this type of problem, we are often only passing through the array once with the two pointers, which means that the time complexity is often O(n).


