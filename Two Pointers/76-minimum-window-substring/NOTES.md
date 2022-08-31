# Intution

This is similar to **Find All Anagrams in a String**, except instead of matching exactly, we are to find a window that contains all characters in check.

In this case, the comparison for checking valid window is changed to compare that for every character in check, see if the window contains more of that character.

In addition, the moving conditions of the window changes as well. Instead of two pointers moving at once, maintaining the size of the window, each pointer moves independently. When the window does not contain check, we move the end pointer until it does (or it reaches the end), then we move the start pointer until the window no longer contains check. In this case, just before moving the window was the local minimal substring. Then it's a simple matter of comparing local minimal substrings and find the minimum one.

**Time Complexity: O(n)**

