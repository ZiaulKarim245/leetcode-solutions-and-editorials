📌 Approach Overview:
We need to check whether we can partition the cards into groups of equal size X ≥ 2, where each group contains cards of the same type.

The key idea is:

Count the frequency of each unique card.

Find the greatest common divisor (GCD) of all frequencies.

If the GCD is at least 2, it's possible to group them as required.

📌 Detailed Steps:
Count Frequencies

Use a dictionary fre_count to count how many times each card number appears in the deck.

Find GCD of All Frequencies

Compute the GCD iteratively for all frequency values.

If the final GCD is greater than 1, it means we can divide the deck into groups of that size.

Decision

If overall_gcd > 1, return True.

Otherwise, return False.
