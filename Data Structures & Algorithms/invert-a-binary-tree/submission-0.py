# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swapSubTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if(node == None):
            return node
        
        left, right = node.left, node.right
        node.left, node.right = right, left
        self.swapSubTree(node.left)
        self.swapSubTree(node.right)
        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root == None):
            return root
        return self.swapSubTree(root)
