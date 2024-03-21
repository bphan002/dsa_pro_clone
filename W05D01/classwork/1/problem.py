class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def gameResult(self, head):
        # Remove pass and write code here

        odd_points = 0
        even_points = 0

        current = head

        while current:
            if current.val > current.next.val:
                even_points +=1
            else: 
                odd_points +=1
            current = current.next.next

        if odd_points > even_points:
            return 'Odd'
        elif even_points > odd_points:
            return 'Even'
        else:
            return 'Tie'