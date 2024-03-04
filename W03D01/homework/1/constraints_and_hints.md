# Search in Rotated Sorted Array Constraints and Hints

## Constraints
-   `1 <= nums.length <= 5000`
-   `-10^4 <= nums[i] <= 10^4`
-   `All values of nums are unique.`
-   `nums is an ascending array that is possibly rotated.`
-   `-10^4 <= target <= 10^4`

## Hint #1
> We can binary search after considering what the mid value is compared to where the left pointer is at.

## Hint #2
> Consider what the value of the mid is compared to the value at the left pointer. What does it mean if the left is larger than the mid?

## Hint #3
> If the left pointer value is larger than the mid value, that means that the mid is currently in the "left sorted portion" of the array