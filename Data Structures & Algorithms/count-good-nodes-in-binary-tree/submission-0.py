# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, mx: int) -> int:
            goodNode = 0 if mx > root.val else 1
            mx = max(mx, root.val)
            if root.left != None:
                goodNode = goodNode + dfs(root.left, mx)
            if root.right != None:
                goodNode = goodNode + dfs(root.right, mx)
            print("Node:", root.val, "GN:", goodNode)
            return goodNode

        return dfs(root, -101)