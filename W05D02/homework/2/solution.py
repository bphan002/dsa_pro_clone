class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head, insertVal):
        if not head:
            node = ListNode(insertVal)
            node.next = node
            return node
        
        current = head
        next_node = head.next
        
        while current:
            
            # case 1: insertVal between smallest and largest vals
            if current.val <= insertVal <= next_node.val:
                current.next = ListNode(insertVal, next_node)
                return head
            # case 2: insertVal between tail and head
            elif current.val > next_node.val and (insertVal >= current.val or insertVal < next_node.val):
                current.next = ListNode(insertVal, next_node)
                return head
            # case 3: all nodes have same val
            elif next_node == head and current.val == next_node.val:
                current.next = ListNode(insertVal, next_node)
                return head

            current = current.next
            next_node = next_node.next