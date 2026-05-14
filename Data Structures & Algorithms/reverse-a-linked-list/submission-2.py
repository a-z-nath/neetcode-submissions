# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, cur, curNext = None, head, head.next
        while cur:
            cur.next = prev
            prev = cur
            cur = curNext
            if cur:
                curNext = cur.next
        return prev