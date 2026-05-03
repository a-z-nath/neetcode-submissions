# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        res = ListNode(0)
        cur = res
        while head != None:
            stack.append(head.val)
            head = head.next
            if len(stack) == k:
                for _ in range(k):
                    cur.next = ListNode(stack.pop())
                    cur = cur.next
        if stack:
            for n in stack:
                cur.next = ListNode(n)
                cur = cur.next
        return res.next