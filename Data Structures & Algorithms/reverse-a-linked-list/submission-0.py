# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        cur = head
        rev_head = None
        while cur != None:
            cur_head = cur
            cur = cur.next
            cur_head.next = rev_head
            rev_head = cur_head
        
        return rev_head