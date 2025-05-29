✅ Solution 1: HashMap (Dictionary)
Idea:
Track the last index where each number appeared.
If the same number appears again within k indices, return True.

Algorithm:

Initialize an empty dictionary.

Iterate over nums with index i.

If nums[i] exists in the dictionary and i - last_index ≤ k, return True.

Otherwise, update nums[i]'s latest index in the dictionary.

If loop ends, return False.

✅ Solution 2: Brute Force with Subarray Check
Idea:
For each element, check if it appears again within the next k elements.

Algorithm:

If nums has no duplicates (compare with set(nums)), return False.

Iterate over nums with index i.

Check if nums[i] exists in nums[i+1:i+1+k].

If yes, return True.

If loop ends, return False.

✅ Solution 3: Sliding Window with Set
Idea:
Maintain a set of the last k numbers.
If a number repeats within this window, return True.

Algorithm:

Initialize an empty set.

Iterate over nums with index i.

If nums[i] exists in the set, return True.

Add nums[i] to the set.

If set size exceeds k, remove nums[i-k].

If loop ends, return False.