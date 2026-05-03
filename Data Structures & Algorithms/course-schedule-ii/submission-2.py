class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        c_list = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            c_list[p].append(c)
        state = [0] * numCourses # 0, 1, 2 => unvisited, visiting, visited
        # dfs only add fully visited, 
        #since you see backside return reverse order.
        c_order = [] 
        def dfs(c):
            # base case
            if state[c] == 1: # visiting => cycle return False
                return False
            if state[c] == 2: # already visited => return True
                return True
            # start visiting add c in c_ord
            state[c] = 1
            for dep_c in c_list[c]:
                if not dfs(dep_c):
                    return False
            state[c] = 2
            c_order.append(c)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return c_order[::-1]
