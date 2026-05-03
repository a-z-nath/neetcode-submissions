# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # for 1 node
        if not fast:
            return
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  if fast.next.next else fast.next
        
        l1, l2 = head, fast
        # reverse n/2 -> n-1
        prev, cur = None, slow.next
        slow.next = None
        print("cur", cur.val)
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur =  temp

        # merge both linked list l1, l2 as head.
        while l1 and l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1, l2 = temp1, temp2
        return None

