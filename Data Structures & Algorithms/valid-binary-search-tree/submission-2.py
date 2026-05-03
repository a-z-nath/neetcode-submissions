# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root: Optional[TreeNode], mn: int, mx: int) -> bool:
            # base case
            if root == None:
                return True


            # recursive calls
            mn1 = min(mn, root.val)
            validBST = True

            if root.val <= mn and root.val > mx:
                validBST = validBST and dfs(root.left, mn1, mx)
            else:
                return False

            mx1 = max(mx, root.val)
            if root.val < mn and root.val > mx:
                validBST = validBST and dfs(root.right, mn, mx1)
            else:
                return False
            return validBST

        return dfs(root, 1111, -1111)
        
