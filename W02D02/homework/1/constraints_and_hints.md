# Valid Parentheses Constraints and Hints

## Constraints
-   `1 <= s.length <= 10^4`
-   `s consists of parentheses only '()[]{}'.`

## Hint #1
> Use a stack of characters.

## Hint #2
> When you encounter an opening bracket, push it to the top of the stack.

## Hint #3
> When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.
