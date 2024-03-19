# Copy List with Random Pointer Constraints and Hints

## Constraints
-   `0 <= n <= 1000`
-   `-10^4 <= Node.val <= 10^4`
-   `Node.random is null or is pointing to some node in the linked list.`

## Hint #1:
> Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from multiple nodes due to the random pointers, ensure you are not making multiple copies of the same node.

## Hint #2: 
> You may want to use extra space to keep old_node ---> new_node mapping to prevent creating multiple copies of the same node.