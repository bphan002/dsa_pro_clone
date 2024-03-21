class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def gameResult(self, head):
        odd = 0
        even = 0
        
        curr = head
        
        while curr:
            if curr.val > curr.next.val:
                even += 1
            elif curr.val < curr.next.val:
                odd += 1
            else:
                continue
            curr = curr.next.next 
        
        if odd > even:
            return "Odd"
        elif even > odd:
            return "Even"
        else:
            return "Tie"