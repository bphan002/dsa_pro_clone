class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def gameResult(self, head):
        odd = 0
        even = 0
        
        even_node = head
        
        while even_node:
            if even_node.val > even_node.next.val:
                even += 1
            else:
                odd += 1

            even_node = even_node.next.next 
        
        if odd > even:
            return "Odd"
        elif even > odd:
            return "Even"
        else:
            return "Tie"