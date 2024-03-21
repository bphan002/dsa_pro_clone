# Linked List Cycle II Constraints and Hints

## Constraints
-   `The number of the nodes in the list is in the range [0, 10^4].`
-   `-10^5 <= Node.val <= 10^5`
-   `pos is -1 or a valid index in the linked-list.`

## Hint #1:
> The easy solution is to use a hash table.

## Hint #2: 
> For the Floyd's Tortoise and Hare Algorithm, first use the usual cycle detection algorithm. When you find the cycle (assuming it exists), create a third pointer at the head. This will be another slow pointer. Iterate until this new pointer meets the slow pointer. The meeting point is the cycle entrance.