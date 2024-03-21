# Split a Circular Linked List Constraints and Hints

## Constraints
-   `The number of nodes in list is in the range [2, 10^5]`
-   `0 <= Node.val <= 10^9`
-   `LastNode.next = FirstNode where LastNode is the last node of the list and FirstNode is the first one`

## Hint #1:
> Do a while loop to calculate the size of the linked list.

## Hint #2: 
> Determine the size of the first half and create a new linked list in its size.

## Hint #3: 
> Do not forget that this half itself should be circular!

## Hint #4: 
> Use the previous hints for the second half.