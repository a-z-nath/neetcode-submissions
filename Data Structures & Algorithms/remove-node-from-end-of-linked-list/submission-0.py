# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for _ in range(n-1):
            if fast.next == None:
                break
            fast = fast.next
        
        slow = None
        while fast.next != None:
            slow = head if slow == None else slow.next
            fast = fast.next
        if slow == None:
            temp = head
            head = head.next
            del temp
        else:
            temp = slow.next
            slow.next = temp.next
            del temp
        return head
        
