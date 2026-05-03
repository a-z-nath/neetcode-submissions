# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BST
# - all node left subtree has smaller value
# - all node right subtree has bigger value
# 	- if both element is greater than cur-root then go right
#   - if both element is less than cur-root then go left
#   - otherwise you got the lca.

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur: TreeNode = root

        while(cur):
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            else:
                return cur