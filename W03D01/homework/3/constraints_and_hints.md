# Koko Eating Bananas Constraints and Hints

## Constraints
-   `1 <= piles.length <= 10^4`
-   `piles.length <= h <= 10^9`
-   `1 <= piles[i] <= 10^9`

## Hint #1:
> The brute force solution would be to go through every possible k value from 1 to the max number in piles. We would calculate the hours of each k value.

## Hint #2: 
> The brute force is iterating through a range between 1 to the max number of piles.

## Hint #3:
> The range is sorted. We can binary search this.