We need to iterate through the sorted list and identify consecutive sequences.

Keep track of the start of each range.

Whenever a number is not consecutive (i.e., nums[i] != nums[i-1] + 1), it means the current range has ended.

Add this range to the result list.

At the end of the list, make sure to add the final range.
