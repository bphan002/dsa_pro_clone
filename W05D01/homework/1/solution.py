class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseListIterative(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
    
    def reverseListRecursive(self, head, prev=None):
        if head is None:
            return prev
        next = head.next
        head.next = prev
        return self.reverseListRecursive(next, head)