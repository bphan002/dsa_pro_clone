# Product of Array Except Self Constraints and Hints

## Constraints
-   `2 <= nums.length <= 10^5`
-   `-30 <= nums[i] <= 30`
-   The product of any prefix or suffix of  `nums`  is  **guaranteed**  to fit in a  **32-bit**  integer.

## Hint #1
> Creating a product lists for the left side and right side could be helpful.

## Hint #2
> Create two lists `left_product` and `right_product` where `left_product[i]` shows the product of all values to the left of the ith element and `right_product[i]` shows the product of all values to the right of the ith element.

## Hint #3
> Multiplying `left_product[i-1]` and `right_product[i+1]` gives the solution.

## Follow up
> Can you solve without using extra space?