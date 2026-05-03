# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast != None:
            slow = slow.next
            fast = fast.next
            fast = fast.next if fast != None else fast
            if fast == None:
                return False
            if slow == fast:
                return True
        return False