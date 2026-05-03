class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        c_list = [[] for _ in range(numCourses)]
        inorder = [0] * numCourses
        for c, p in prerequisites:
            c_list[p].append(c)
            inorder[c] += 1
        # with inorder + bfs + queue
        q = deque()
        c_order = []
        for i in range(numCourses):
            if inorder[i] == 0:
                q.append(i)
        while len(q) > 0:
            # pop q, add c_o, dec ino[c] =>0 -> push c
            p = q.popleft()
            c_order.append(p)
            for c in c_list[p]:
                inorder[c] -= 1
                if inorder[c] == 0:
                    q.append(c)
        if len(c_order) != numCourses:
            return []
        return c_order