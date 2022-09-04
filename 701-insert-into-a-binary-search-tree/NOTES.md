One of the advantages to using a BST compared to a sorted list (to keep track of which items exist in a collection) is that, unlike a sorted list, inserting an item to the BST does not require each item in the list to move down an index, like inserting to a sorted list do.
​
Instead, when inserting an item, first perform the searching for that item in that BST. However, if we find an empty tree, instead we replace that empty tree with a new node containing the inserted value in the BST.
​
​