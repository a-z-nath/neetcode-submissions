# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        def reverse(head: ListNode) -> ListNode:
            prev, cur = None, head
            while cur:
                curNext = cur.next
                cur.next = prev
                prev, cur = cur, curNext
            return prev
        slow, fast = head, head
        while fast:
            fast = None if not fast.next else fast.next.next
            if not fast:
                tmp = slow.next
                slow.next = None
                slow = tmp
                break
            slow = slow.next
        rev = reverse(slow)
        
        # merge
        cur = head
        while cur and rev:
            curNext, revNext = cur.next, rev.next
            cur.next, rev.next = rev, curNext
            cur, rev = curNext, revNext
            
        
