# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root == None):
            return []
        
        def bfs(root: TreeNode) -> List[List[int]]:
            queue : List[TreeNode]= [root]
            levels : List[List[int]] = []
            while len(queue) > 0:
                level : List[int] = []
                size = len(queue)
                for i in range(0, size):
                    temp: TreeNode = queue[0]
                    queue.pop(0)
                    level.append(temp.val)
                    if temp.left != None:
                        queue.append(temp.left)
                    if temp.right != None:
                        queue.append(temp.right)
                
                levels.append(level)
            return levels
        return bfs(root)