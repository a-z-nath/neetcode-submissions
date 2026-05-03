# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    result = None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # base case
        if not root:
            return -1

        # recursive calls
        kthNum = self.kthSmallest(root.left, k)
        self.count = self.count + 1
        if self.count == k:
            self.result = root.val
            return root.val
        kthNum = max(kthNum, self.kthSmallest(root.right, k))
        return kthNum