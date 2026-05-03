class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 => not visited, 1 => visiting, 2 => visited
        states = [0] * numCourses
        courses = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            courses[p].append(c)
        def dfs(crs):
            if states[crs] == 1:
                return False
            if states[crs] == 2:
                return True
            
            states[crs] = 1
            for c in courses[crs]:
                if not dfs(c):
                    return False
            states[crs] = 2
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True