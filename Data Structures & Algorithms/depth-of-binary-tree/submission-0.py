# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pre_order(self, node: Optional[TreeNode]) -> int:
        if(node == None):
            return 0
        depth = 1
        depth = depth + max(self.pre_order(node.left), self.pre_order(node.right))
        return depth
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return 0
        return self.pre_order(root)
