# Find Peak Element Constraints and Hints

## Constraints
-   `1 <= nums.length <= 1000`
-   `-2^31 <= nums[i] <= 2^31 - 1`
-   `nums[i] != nums[i + 1] for all valid i.`

## Hint #1
> If you compare the current element with its neighbors and find one is larger while the other is smaller, can we select one direction that will guarantee a peak?

## Hint #2
> If you keep following larger numbers, you are guaranteed to reach a peak or hit the end of the array (which can possibly be a peak since we consider out of bounds as negative infinity).
