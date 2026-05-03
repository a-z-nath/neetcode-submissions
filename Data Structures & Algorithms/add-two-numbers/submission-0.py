# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, total = 0, 0
        res = ListNode(0)
        head = res
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total // 10
            total %= 10
            cur = ListNode(total)
            res.next = cur
            res = cur
            l1, l2 = l1.next, l2.next
        while l1:
            total = l1.val + carry
            carry = total // 10
            total %= 10
            cur = ListNode(total)
            res.next = cur
            res = cur
            l1 = l1.next
        while l2:
            total = l2.val + carry
            carry = total // 10
            total %= 10
            cur = ListNode(total)
            res.next = cur
            res = cur
            l2 = l2.next
        if carry > 0:
            cur = ListNode(carry)
            res.next =cur
        return head.next