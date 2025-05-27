✅ Approach 1: Sorting and Comparing Neighbors
Idea:
Sort the array so that any duplicate elements will be adjacent. Then, iterate through the list and compare each element with the one before it. If two consecutive elements are the same, a duplicate exists.

✅ Approach 2: Using a Set
Idea:
A set only stores unique values. Convert the list to a set and compare its length to the original list. If the lengths differ, duplicates exist.

✅ Approach 3: Using collections.Counter
Idea:
Use Counter from the collections module to count the frequency of each element. If any element has a frequency greater than 1, a duplicate exists.
