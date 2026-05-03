# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0
    def post_order(self, node: Optional[TreeNode]) -> int:
        if(node == None):
            return 0
        l_height, r_height = self.post_order(node.left), self.post_order(node.right)
        height = 1 + max(l_height, r_height)
        self.diameter = max(self.diameter, l_height + r_height)
        return height

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return self.diameter
        self.post_order(root)
        return self.diameter