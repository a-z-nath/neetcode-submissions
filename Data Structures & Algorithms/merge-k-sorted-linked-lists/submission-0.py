# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) <= 0:
            return None
        res = ListNode(0)
        cur = res
        while True:
            minNode = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minNode == -1 or lists[minNode].val > lists[i].val:
                    minNode = i
            if minNode == -1:
                break
            cur.next = ListNode(lists[minNode].val)
            lists[minNode] = lists[minNode].next
            cur = cur.next
        return res.next