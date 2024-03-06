#  Jump Game Constraints and Hints

## Constraints
-   `1 <= nums.length <= 10^4`
-   `0 <= nums[i] <= 10^5`

## Hint #1:
> What if we iterate backwards?

## Hint #2: 
> If we iterate backwards, how can we know whether a position can reach the end?

## Hint #3:
> Set the target to be the end of the array. As you iterate backwards and find indices that can reach the target, update your target to that index since you know that any index that can reach that new target will also be able to reach the end.