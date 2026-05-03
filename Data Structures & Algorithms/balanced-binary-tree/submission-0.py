# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balanceHeight = True
    def heightBanlanceCheck(self, node: Optional[TreeNode]) -> int:
        if(self.balanceHeight == False):
            return 0
        if(node == None):
            return 0
        l_height, r_height = self.heightBanlanceCheck(node.left), self.heightBanlanceCheck(node.right)
        
        if(abs(l_height - r_height) > 1):
            self.balanceHeight = False
        
        return 1 + max(l_height, r_height)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(root == None):
            return True
        self.heightBanlanceCheck(root)
        return self.balanceHeight
        