The problem can be efficiently solved using a single pass greedy algorithm. The idea is to keep track of:

the minimum price so far (best day to buy), and

the maximum profit possible so far based on the current price and this minimum price.

At each step:

Update the minimum price if the current price is lower.

Compute the profit by selling at the current price after buying at the minimum price so far.

Update the maximum profit if this new profit is better than the previous maximum.
