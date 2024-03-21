# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head


        '''      
                                     c 
                    Input: head = [1,2,6,3,4,5,6], val = 6
                                       N
                                   p
                    Output: [1,2,3,4,5]
        '''
        while curr:
            next = curr.next
            if curr.val == val:
                prev.next = next
            else:
                prev = curr
            curr = next
        print('head', dummy.next)
        return dummy.next