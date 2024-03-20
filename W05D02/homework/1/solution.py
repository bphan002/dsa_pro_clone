import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitCircularLinkedList(self, head):
        nodes = 0
        current = head
        tail = None
        
        while current:
            nodes += 1
            if current.next == head:
                tail = current
                current = current.next
                break
            current = current.next
            
        half = math.ceil(nodes/2)
        nodes = 0

        while current:
            nodes += 1
            
            if nodes == half:
                head2 = current.next
                current.next = head
                tail.next = head2
                return [head, head2]
            
            current = current.next