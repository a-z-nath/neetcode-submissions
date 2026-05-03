# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        l1, l2 = list1, list2
        dummy = ListNode(float("-inf"))
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = l1
                l1 = l1.next
            else:
                cur.next = l2
                cur = l2
                l2 = l2.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return dummy.next