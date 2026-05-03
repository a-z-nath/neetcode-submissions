# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev, cur, curNext= None, head, head.next
        while cur:
            # build link
            cur.next = prev
            if curNext == None:
                return cur
            # update linker var
            prev = cur
            cur = curNext
            curNext = curNext.next
        return cur