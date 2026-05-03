# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        def bfs(root: TreeNode) -> List[int]:
            queue : List[TreeNode]= [root]
            rightView: List[int] = []
            while len(queue) > 0:
                size = len(queue)
                rightView.append(queue[size-1].val)
                for i in range(0, size):
                    temp: TreeNode = queue[0]
                    queue.pop(0)
                    if temp.left != None:
                        queue.append(temp.left)
                    if temp.right != None:
                        queue.append(temp.right)
                
            return rightView

        return bfs(root)