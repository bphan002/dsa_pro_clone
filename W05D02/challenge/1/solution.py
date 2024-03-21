class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head):
        if head == None or head.next == None: return None
        slow, fast = head, head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                slow2 = head
                while True:
                    if slow == slow2: return slow
                    slow = slow.next
                    slow2 = slow2.next

        return None