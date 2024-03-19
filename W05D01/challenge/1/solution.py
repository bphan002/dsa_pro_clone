class ListNode:
    def __init__(self, val, next=None, random=None, index=0):
        self.val = val
        self.next = next
        self.random = random
        self.index = index

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        hash_map = {None: None}
        
        new_head = ListNode(head.val, None, None)
        
        current = head
        
        while current:
            new_node = ListNode(current.val, None, None)
            hash_map[current] = new_node
            current = current.next
            
        current = head
        
        while current:
            hash_map[current].next = hash_map[current.next]
            hash_map[current].random = hash_map[current.random]
            current = current.next
            
        return hash_map[head]