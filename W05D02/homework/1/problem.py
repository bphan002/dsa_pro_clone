import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitCircularLinkedList(self, head):
        # Remove pass and write code here
        curr = head
        output = [[],[]]
        length = 0

        visited = set()

    
        while curr not in visited:
            visited.add(curr)
            # visited.add(curr.val)
            curr = curr.next

        linklist_size = len(visited)
        first_half = math.ceil(linklist_size//2)
        second_half = linklist_size - first_half
        nodes = 0
        current = head
        while current:
            nodes +=1
            
            if nodes == first_half:
                head2 = current.next
                current.next = head
                tail.next = head2
                return [head, head2]
            
            current = current.next