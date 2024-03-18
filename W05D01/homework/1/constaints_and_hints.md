#  Reverse Linked List Constraints and Hints

## Constraints
-   `The number of nodes in the list is the range [0, 5000].`
-   `-5000 <= Node.val <= 5000`

## Hint #1:
> As you traverse, it could be useful to keep track of your previous node in addition to the current node.

## Hint #2: 
> Update all pointers for each node. The current node's next pointer should now point to the previous node. You may have to save a reference to the next node before reassigning in order to continue traversing.