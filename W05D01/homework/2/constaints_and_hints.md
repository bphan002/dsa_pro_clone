# Remove Nth Node From End of List Constraints and Hints

## Constraints
-   `The number of nodes in the list is sz.`
-   `1 <= sz <= 30`
-   `0 <= Node.val <= 100`
-   `1 <= n <= sz`

## Hint #1:
> A two pointer approach could be useful. If the second pointer is always n steps ahead of the first pointer, where will that first pointer be when the second one reaches the end of the list?

## Hint #2:
> As you traverse, it could be useful to keep track of your previous node in addition to the current node.

## Hint #3: 
> You may potentially have to remove the head node. Use a dummy node to always reference the current head node.