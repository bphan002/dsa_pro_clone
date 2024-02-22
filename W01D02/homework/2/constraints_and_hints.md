# Group the People Given the Group Size They Belong To Constraints and Hints

## Constraints
-   `groupSizes.length == n`
-   `1 <= n <= 500`
-   `1 <= groupSizes[i] <= n`

## Hint #1
> Using a hash map to keep track of groups could be useful.

## Hint #2
> How do we know if we have created a valid group?

## Hint #3
> If we compile lists for each group and it reaches capacity, simply a append this to a results array and clear out you group list.